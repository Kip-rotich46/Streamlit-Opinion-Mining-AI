# help.py

import streamlit as st

def help(conn):
    st.title("Welcome to Opinion Mining AI help page")
    st.write("This is the Help page.")
    st.write("A help page for sentiment analysis would serve as a comprehensive guide for users seeking assistance with understanding and utilizing sentiment analysis techniques effectively. It would typically provide an overview of sentiment analysis, explaining its purpose and significance in various fields such as marketing, customer feedback analysis, and social media monitoring. The help page would detail different approaches to sentiment analysis, including lexicon-based methods, machine learning algorithms, and deep learning techniques. It would offer guidance on selecting appropriate sentiment analysis tools and libraries, outlining their features and capabilities. Additionally, the help page might include tips for preprocessing text data, handling sentiment polarity, and evaluating sentiment analysis models' performance. It could also provide sample code snippets or tutorials to help users get started with sentiment analysis implementation in their projects. Overall, the help page would aim to empower users with the knowledge and resources needed to successfully apply sentiment analysis to their data analysis tasks.")
    
    st.subheader("Have a Question?")
    st.write("If you have any questions or need further assistance, you can submit your query below.")

    # Input field for user's email
    email = st.text_input("Enter your email:")

    # Input field for user's WhatsApp number
    whatsapp = st.text_input("Enter your WhatsApp number (include country code):")

    # Text area for user's question
    question = st.text_area("Enter your question:")

    # Button to submit the question
    if st.button("Submit Question"):
        if not question.strip():
            st.error("Please enter your question before submitting.")
        else:
            # Submit the question if it's not empty
            send_question(email, whatsapp, question)
        # Assuming you have a function to send emails or WhatsApp messages
        

def send_question(email, whatsapp, question):
    # Implement logic to send the question via email or WhatsApp
    # You can use external libraries or APIs for this purpose
    # For example, if using the 'smtplib' library for sending emails:
    import smtplib

    # SMTP server configuration
    smtp_server = 'elasticemail.com'
    smtp_port = 587
    sender_email = 'your_email@example.com'
    receiver_email = 'protiolangat468@gmail.com'
    password = '8257Giddy'

    # Email content
    subject = 'Question from Help Page'
    body = f"Email: {email}\nWhatsApp: {whatsapp}\nQuestion: {question}"

    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
    server.starttls()
    server.login(sender_email, password)

    # Send email
    server.sendmail(sender_email, receiver_email, f'Subject: {subject}\n\n{body}')

    # Close connection
    server.quit()

if __name__ == '__main__':
    help(None)  # Pass None for the 'conn' argument as it's not used in this function
