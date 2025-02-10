import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StdOutCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title="Langchain: CHat with SQL Databse")
st.title("Langhain Chat WIth SQL Database")

LOCALDB = "USE_LOCALDB"
MYSQL= "USE_MYSQL"

radio_opt=["Use SQLlite 3 Database- Student.db","Connect to your SQL Database"]
selected_opt = st.sidebar.radio(label="Choose the DB you want to chat with", options=radio_opt)

if radio_opt.index(selected_opt) == 1:
    db_url = MYSQL
    mysql_host = st.sidebar.text_input("Provide my SQL Host")
    mysql_user = st.sidebar.text_input("MYSQL User")
    mysql_password = st.sidebar.text_input("MYSQL Password", type="password")
    mysql_db = st.sidebar.text_input("MySQL Database")
else:
    db_url = LOCALDB

api_key = st.sidebar.text_input(label="GROQ Api Key", type="password")

if not db_url:
    st.info("Please enter the database information and url")

if not api_key:
    st.info("Please add the GROQ API key")

ChatGroq(groq_api_key = api_key, model_name="Llama3-8b-8192", streaming=True)

@st.cache_resource(ttl="2h")
def configure_db(db_url, mysql_host=None,mysql_user=None,mysql_password=None,mysql_db=None):
    if db_url == LOCALDB:
        db_filepath=(Path(__file__).parent/"student.db").absolute()
        print(db_filepath)
        creator = lambda: sqlite3.connect(f"file:{db_filepath}?mode=ro", url=True)
        return SQLDatabase(create_engine("sqlite:///", creatoe=creator))
    elif db_url == MYSQL:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please provide all MySQL COnnection Details")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))
    
if db_url == MYSQL:
    db=configure_db(db_url, mysql_host, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db=configure_db(db_url)

