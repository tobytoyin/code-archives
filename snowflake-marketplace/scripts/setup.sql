CREATE APPLICATION ROLE app_public;
CREATE SCHEMA IF NOT EXISTS streamlit_app;
GRANT USAGE ON SCHEMA streamlit_app TO APPLICATION ROLE app_public;

-- create streamlit app entry point
CREATE STREAMLIT streamlit_app.my_streamlit_app
  FROM '/src'
  MAIN_FILE = '/main.py'
;

GRANT USAGE ON STREAMLIT streamlit_app.my_streamlit_app TO APPLICATION ROLE app_public;