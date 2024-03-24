import streamlit as st
import datetime as dt
import os
from dotenv import load_dotenv
import requests
import base64

# Load environment variables
load_dotenv()
COGNITO_DOMAIN = os.environ.get("COGNITO_DOMAIN")
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
APP_URI = os.environ.get("APP_URI")

# Define the last couple of days
days = dt.timedelta(days=3)
end_date = dt.datetime.now()
start_date = end_date - days

# Load registered users and their login activities
# This is a placeholder, replace it with your actual data source
registered_users = ['user1', 'user2', 'user3']
logins = {'user1': 2, 'user2': 1, 'user3': 0}
uploaded_files = {'user1': ['file1.txt', 'file2.txt'], 'user2': ['file3.txt'], 'user3': []}

# Check if the user is logged in as admin
if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
    # Display login button
    if st.button('Login as admin'):
        # Redirect to the authentication page
        st.experimental_set_page_config(page_title="Login", page_icon="🔒")
        st.markdown("# Login")
        st.sidebar.header("Login")
        username = st.text_input('Enter your username:')
        password = st.text_input('Enter your password:', type='password')
        if st.button('Login'):
            # Authenticate the user
            auth_code = authenticate_user(username, password)
            if auth_code:
                # Get user tokens
                access_token, id_token = get_tokens(auth_code)
                if access_token and id_token:
                    # Set the user as authenticated
                    st.session_state['authenticated'] = True
                    st.session_state['access_token'] = access_token
                    st.session_state['id_token'] = id_token
                    st.write('You are now logged in as admin.')
                    # Add code here to display the admin page
                else:
                    st.write('Authentication failed.')
            else:
                st.write('Authentication failed.')
        else:
            st.write('')
else:
    st.write('Welcome, admin!')

# Display registered users
st.subheader('Registered Users')
for user in registered_users:
    st.write(user)

# Display login activity
st.subheader('Login Activity in the Last Couple of Days')
st.write(sum(list(logins.values())))
for user, n in logins.items():
    st.write(f'{user}: {n} logins')

# Display uploaded files
st.subheader('Uploaded Files')
for user, files in uploaded_files.items():
    st.write(user)
    for file in files:
        st.write(file)

# Display logins in a pie chart
st.subheader('Logins')
activities = list(logins.values())
labels = list(logins.keys())
st.pie(activities, labels=labels)

# Function to authenticate the user
def authenticate_user(username, password):
    # Send a request to the authentication API
    response = requests.post(
        f"https://{COGNITO_DOMAIN}/oauth2/token",
        data={
            "grant_type": "password",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "username": username,
            "password": password,
            "scope": "openid email phone profile",
        },
    )
    # Check if therequest was successful
    if response.status_code == 200:
        # Extract the authorization code from the response
        auth_code = response.json().get("access_token")
        return auth_code
    else:
        return None

# Function to get user tokens
def get_tokens(auth_code):
    # Send a request to the token API
    response = requests.post(
        f"https://{COGNITO_DOMAIN}/oauth2/token",
        data={
            "grant_type": "authorization_code",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": auth_code,
            "redirect_uri": APP_URI,
        },
    )
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the access token and ID token from the response
        access_token = response.json().get("access_token")
        id_token = response.json().get("id_token")
        return access_token, id_token
    else:
        return None