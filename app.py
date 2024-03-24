import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from registration import registration
from login import login
from sentiment import sentiment
from help import help
from file_upload import file_upload
from login_register import *

# Create a connection to the SQLite database
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# Create a table to store user details if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')

# Initialize session state
if 'is_registered' not in st.session_state:
    st.session_state['is_registered'] = False

# Main function
def main():
    st.set_page_config(layout="wide")
        
    # Get the current page name
    page = st.sidebar.selectbox("Select a page", ["Home", "Login/Register", "About"])
    
    # Display the about page
    if page == "About":
        about(conn)  # Pass the conn object to the about() function
    else:
        # Check if the user is registered
        if not st.session_state.get('is_registered', False):
            login_register(conn)  # If not registered, display login/register page
        else:
            # If registered, display dashboard page
            st.session_state['username'] = st.session_state['username']
            dashboard(conn)
    
        
if __name__ == '__main__':
    main()