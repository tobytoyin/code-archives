package_name=$1
app_name=$2
stage_name=$3  # my_streamlit_package.public.package_stage

snowsql -q "
use role accountadmin; 

-- setup previlages
GRANT CREATE APPLICATION PACKAGE ON ACCOUNT TO ROLE ACCOUNTADMIN; 
GRANT CREATE APPLICATION ON ACCOUNT TO ROLE ACCOUNTADMIN;

-- create a package placeholder 
CREATE APPLICATION PACKAGE $package_name;
GRANT INSTALL ON APPLICATION PACKAGE $package_name TO ROLE ACCOUNTADMIN;    
SHOW APPLICATION PACKAGES;

USE APPLICATION PACKAGE $package_name;
CREATE OR REPLACE STAGE $stage_name
FILE_FORMAT = (TYPE = 'csv' FIELD_DELIMITER = '|' SKIP_HEADER = 1);
"

# snowflake PUT doesn't allow dir sync, so we'll have to use a for-loop to PUT
for file in ./src/*; do
    snowsql -q "
        USE APPLICATION PACKAGE $package_name;
        PUT file://${file} @$stage_name/streamlit/$(basename $file) overwrite=true auto_compress=false;"
done

# manifest, setup.sql, readme
snowsql -q "
USE APPLICATION PACKAGE $package_name;
PUT file://./manifest.yml @$stage_name/manifest.yml overwrite=true auto_compress=false;
PUT file://./scripts/setup.sql @$stage_name/scripts/setup.sql overwrite=true auto_compress=false;
PUT file://./README.md @$stage_name/README.md overwrite=true auto_compress=false;
"

# build the package application
snowsql -q "
--- create application
USE APPLICATION PACKAGE $package_name;

CREATE APPLICATION $app_name
FROM APPLICATION PACKAGE $package_name
USING '@$stage_name';
"

# set up package version
snowsql -q "
-- set streamlit version
USE APPLICATION PACKAGE $package_name;

ALTER APPLICATION PACKAGE $package_name
ADD VERSION v1_0 USING '@$stage_name';

-- set package version
ALTER APPLICATION PACKAGE $package_name
    SET DEFAULT RELEASE DIRECTIVE
    VERSION = v1_0
    PATCH = 0;
"