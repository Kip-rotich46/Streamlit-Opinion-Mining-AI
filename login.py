# login.py module

import streamlit as st

def login(conn):
    st.title('Login Page')
    
    # Add login inputs
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    
    # Check if username and password match
    if st.button('Login'):
        if username and password:
            c = conn.cursor()  # Create cursor object
            c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = c.fetchone()
            if user:
                st.success('Logged in as {}'.format(username))
                return username  # Return the username if login is successful
            else:
                st.error('Invalid username or password')
        else:
            st.warning('Please enter both a username and password.')
