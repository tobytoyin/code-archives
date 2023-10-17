

-- create a stage to upload application to PACKAGE
USE APPLICATION PACKAGE my_streamlit_package;


-- run the below using the connector/ api
PUT file:///./ @my_streamlit_package overwrite=true auto_compress=false;
PUT file:///
-- PUT file:///<path_to_your_root_folder>/tutorial/scripts/setup.sql @hello_snowflake_package.stage_content.hello_snowflake_stage/scripts overwrite=true auto_compress=false;
-- PUT file:///<path_to_your_root_folder>/tutorial/readme.md @hello_snowflake_package.stage_content.hello_snowflake_stage overwrite=true auto_compress=false;

-- -- files in package
-- LIST @MY_STREAMLIT_PACKAGE.PUBLIC.PACKAGE_STAGE;

-- -- install application
-- CREATE APPLICATION my_streamlit_app
--   FROM APPLICATION PACKAGE MY_STREAMLIT_PACKAGE
--   USING '@MY_STREAMLIT_PACKAGE.PUBLIC.PACKAGE_STAGE';
  

-- ----- ABOVE ARE SETUP ONLY RUN ONCE -----
  
-- -- set streamlit version
-- ALTER APPLICATION PACKAGE MY_STREAMLIT_PACKAGE
--   ADD VERSION v1_0 USING '@MY_STREAMLIT_PACKAGE.PUBLIC.PACKAGE_STAGE';


-- -- set package version
-- SHOW VERSIONS IN APPLICATION PACKAGE MY_STREAMLIT_PACKAGE;
-- ALTER APPLICATION PACKAGE MY_STREAMLIT_PACKAGE
--   SET DEFAULT RELEASE DIRECTIVE
--   VERSION = v1_0
--   PATCH = 0;

-- -- install and show up in app sidebar in snowflake
-- SHOW APPLICATIONS;
-- USE APPlICATION my_streamlit_app;

-- -- scan and publish to external
-- ALTER APPLICATION PACKAGE MY_STREAMLIT_PACKAGE SET DISTRIBUTION = EXTERNAL;