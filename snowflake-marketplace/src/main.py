# Import python packages
import openai
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Hello Snowflake - Streamlit Edition")
st.write(
    """The following data is from the accounts table in the application package.
      However, the Streamlit app queries this data from a view called
      code_schema.accounts_view.
   """
)
