import streamlit as st
import sqlite3
from dashboard import *

from app import conn

def login_register(conn):
    st.subheader("Login or Register")
    
    # Username input
    username = st.text_input("Username")
    
    # Password input
    password = st.text_input("Password", type="password")
    
    # Login button
    if st.button("Login"):
        try:
            # Check if the username and password fields are not empty
            if not username or not password:
                raise ValueError("Please enter both username and password.")
            
            # Check if the user exists and the password is correct
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            result = c.fetchone()
            
            if result:
                st.session_state['is_registered'] = True
                st.session_state['username'] = username
                dashboard(conn)  # If logged in, redirect to the dashboard page
            else:
                st.error("Invalid username or password")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    # Registration button
    if st.button("Register"):
        try:
            # Check if the username and password fields are not empty
            if not username or not password:
                raise ValueError("Please enter both username and password.")
            
            # Check if the username is already taken
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE username = ?", (username,))
            result = c.fetchone()
            
            if result:
                st.error("Username already taken")
            else:
                # If the username is available, register the user
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                
                st.session_state['is_registered'] = True
                st.session_state['username'] = username
                dashboard(conn)  # If registered, redirect to the dashboard page
        except Exception as e:
            st.error(f"An error occurred: {e}")
