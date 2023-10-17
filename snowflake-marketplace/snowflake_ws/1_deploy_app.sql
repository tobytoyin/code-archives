

-- create a stage to upload application to PACKAGE
USE APPLICATION PACKAGE my_streamlit_package;


-- run the below using the connector/ api

-- -- files in package
-- LIST @MY_STREAMLIT_PACKAGE.PUBLIC.PACKAGE_STAGE;

-- -- install application

  

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