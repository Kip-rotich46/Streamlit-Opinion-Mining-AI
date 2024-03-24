# registration.py module

import streamlit as st
from login import login

def registration(conn):
    st.title('User Registration')
    
    # Add registration inputs
    new_username = st.text_input('Enter a new username')
    new_password = st.text_input('Enter a new password', type='password')
    
    # Add a button to register
    if st.button('Register'):
        if new_username and new_password:
            c = conn.cursor()  # Create cursor object
            # Check if the username already exists
            c.execute("SELECT * FROM users WHERE username=?", (new_username,))
            existing_user = c.fetchone()
            if existing_user:
                st.error('Username already exists. Please choose a different username.')
            else:
                # Save new user details to the database
                c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, new_password))
                conn.commit()
                st.success('Registration successful! Please proceed to login.')
                
                # Set the is_registered state to True
                st.session_state['is_registered'] = True
                st.session_state['new_username'] = new_username  # Save the new username
        else:
            st.warning('Please enter both a username and password.')
            
        login(c)