set -e

PACKAGE_NAME=$1
APP_NAME=$2
STAGE_NAME=$3  # my_streamlit_package.public.package_stage

PACKAGE_STG_NAME="$PACKAGE_NAME.PUBLIC.$STAGE_NAME"


# write setup.sql based on inputs
streamlit_schema="STREAMLIT_APP"
echo "
--The following is within the context of '$APP_NAME'

CREATE APPLICATION ROLE app_public;
CREATE SCHEMA IF NOT EXISTS $streamlit_schema;
GRANT USAGE ON SCHEMA DEMO TO APPLICATION ROLE app_public;

-- create streamlit app entry point
CREATE STREAMLIT $streamlit_schema.$APP_NAME
  FROM '/streamlit'
  MAIN_FILE = '/main.py'
;
GRANT USAGE ON STREAMLIT $streamlit_schema.$APP_NAME TO APPLICATION ROLE app_public;
" > ./scripts/setup.sql



snowsql -q "
use role accountadmin;

-- setup previlages
GRANT CREATE APPLICATION PACKAGE ON ACCOUNT TO ROLE ACCOUNTADMIN;
GRANT CREATE APPLICATION ON ACCOUNT TO ROLE ACCOUNTADMIN;

-- create a package placeholder
CREATE APPLICATION PACKAGE $PACKAGE_NAME;
GRANT INSTALL ON APPLICATION PACKAGE $PACKAGE_NAME TO ROLE ACCOUNTADMIN;
SHOW APPLICATION PACKAGES;

USE APPLICATION PACKAGE $PACKAGE_NAME;
CREATE OR REPLACE STAGE $STAGE_NAME
FILE_FORMAT = (TYPE = 'csv' FIELD_DELIMITER = '|' SKIP_HEADER = 1);
"

# snowflake PUT doesn't allow dir sync, so we'll have to use a for-loop to PUT
streamlit_files=$( find ./src -type f | xargs )  # ensure n-depth tree
for file in $streamlit_files ; do
    snowsql -q "PUT\
    file://${file} @$PACKAGE_STG_NAME/streamlit overwrite=true auto_compress=false;"
done

# manifest, setup.sql, readme
snowsql -q "\
PUT file://./manifest.yml @$PACKAGE_STG_NAME overwrite=true auto_compress=false;
PUT file://./scripts/setup.sql @$PACKAGE_STG_NAME/scripts overwrite=true auto_compress=false;
PUT file://./README.md @$PACKAGE_STG_NAME overwrite=true auto_compress=false;
"

# build the package application
snowsql -q "
--- create application
CREATE APPLICATION $APP_NAME
FROM APPLICATION PACKAGE $PACKAGE_NAME
USING '@$PACKAGE_STG_NAME';
"

# set up package version
snowsql -q "
-- set streamlit version
USE APPLICATION PACKAGE $PACKAGE_NAME;

ALTER APPLICATION PACKAGE $PACKAGE_NAME
ADD VERSION v1_0 USING '@$STAGE_NAME';

-- set package version
ALTER APPLICATION PACKAGE $PACKAGE_NAME
    SET DEFAULT RELEASE DIRECTIVE
    VERSION = v1_0
    PATCH = 0;
"

# scan the app and start it
snowsql -q "
SHOW APPLICATIONS;
USE APPlICATION $APP_NAME;

ALTER APPLICATION PACKAGE $PACKAGE_NAME SET DISTRIBUTION = EXTERNAL;
"
