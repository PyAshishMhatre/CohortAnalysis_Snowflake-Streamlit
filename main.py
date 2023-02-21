import pandas as pd
import numpy as np
import streamlit as st
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import avg, sum, col,lit

def create_session_object():
   connection_parameters = {
      "account": "",
      "user": "",
      "password": "",
      "role": "",
      "warehouse": "",
      "database": "",
      "schema": ""
   }
   session = Session.builder.configs(connection_parameters).create()
   return session


def load_data(session,table_name):
    # CO2 Emissions by Country
    # Complete database
    df_trans = session.table(table_name)
    df_trans = df_trans.to_pandas()
    return df_trans


session = create_session_object()
data = load_data(session,'biketransactions')


print(data.head())

session.close()
