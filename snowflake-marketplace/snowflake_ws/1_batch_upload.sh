

stage_name=$1  # my_streamlit_package.public.package_stage

# snowflake PUT doesn't allow dir sync, so we'll have to use a for-loop to PUT
for file in ./src/*; do
    snowsql -q "PUT \
        file://${file} @$stage_name/streamlit/$(basename $file) \
        overwrite=true auto_compress=false"
done

# manifest, setup.sql, readme
snowsql -q "PUT file://./manifest.yml @$stage_name/manifest.yml overwrite=true auto_compress=false"
snowsql -q "PUT file://./scripts/setup.sql @$stage_name/scripts/setup.sql overwrite=true auto_compress=false"
snowsql -q "PUT file://./README.md @$stage_name/README.md overwrite=true auto_compress=false"


# install application
echo "Installing application"