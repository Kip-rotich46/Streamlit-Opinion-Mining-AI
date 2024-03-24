import streamlit as st
from sentiment import *
from about import *
import sqlite3
from help import *
from file_upload import *

conn = sqlite3.connect('user_data.db')
c = conn.cursor()

def dashboard(conn):
    

    # Sidebar navigation
    page = st.sidebar.radio("Navigate",["file_upload","Sentiment Analysis","About","Help"])

    if page == "About":
        about(conn)
    elif page == "Sentiment Analysis":
        sentiment(conn)
    elif page == "file_upload":
        file_upload()
    elif page == "Help":
        help(conn)