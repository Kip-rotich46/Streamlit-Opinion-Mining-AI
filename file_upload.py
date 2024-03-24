# file_upload.py

import streamlit as st
from sentiment import *

def file_upload():
    st.title('File Upload Page')
    st.write('For file upload, only CSV files are supported.')
    st.write('This files will undergo sentiment analysis and the result displayed in the sentiment analysis page.')
    
    # File uploader widget
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    # Check if file is uploaded
    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        
        # Display some information about the uploaded file
        st.write("Uploaded file details:")
        st.write(uploaded_file)
        sentiment()
