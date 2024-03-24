# recommendations.py

import streamlit as st

def recommendations():
    st.title('Recommendations')
    st.write("Here are some recommendations based on the sentiment analysis results.")
    st.write("Your dataset had a staggering 4162 Positive score that is a percentage of 84.7%,469 Negative score 9.54%,284 Neutral score 5.78%")
    # Add your recommendation content here
    st.write("Continue with the good work")
    
if __name__ == '__main__':
    recommendations()
