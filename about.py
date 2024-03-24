import streamlit as st

def about(conn):
    st.title("Welcome to Opinion Mining AI")
    with open("components/about.html") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.write("This is the About page.")
        st.write("Opinion Mining AI is a web application that uses natural language processing techniques to analyze the sentiment of text data.")
        st.write("The app uses a SQLite database to store user information and session state.")
        st.write("An 'About' page for a sentiment analysis application provides users with essential information about the purpose, functionality, and significance of sentiment analysis. It serves as a resource to educate users and enhance their understanding of the application. Here's a draft for an 'About' page:")
        st.write("---")
        st.write("# About Sentiment Analysis")

        st.write("Welcome to our sentiment analysis application! Sentiment analysis is a powerful tool used to analyze and understand the sentiment expressed in text data. This application utilizes sentiment analysis techniques to provide valuable insights into the emotions and opinions conveyed in textual content.")

        st.write("## What is Sentiment Analysis?")

        st.write("Sentiment analysis, also known as opinion mining, is the process of determining the sentiment or emotional tone conveyed in a piece of text. It involves analyzing text data to identify and classify subjective information, such as positive, negative, or neutral sentiments.")

        st.write("## How Does Sentiment Analysis Work?")

        st.write("Sentiment analysis algorithms use natural language processing (NLP) techniques to analyze text data and extract sentiment-related information. These algorithms examine various linguistic features, such as words, phrases, and context, to determine the sentiment expressed in the text.")

        st.write("## Why Use Sentiment Analysis?")

        st.write("Sentiment analysis has a wide range of applications across various industries and domains. It can be used to:")

        st.write("- **Customer Feedback Analysis**: Analyze customer reviews, comments, and feedback to understand customer sentiment towards products or services.")
        st.write("- **Social Media Monitoring**: Monitor social media posts, tweets, and comments to gauge public opinion and sentiment on specific topics or brands.")
        st.write("- **Market Research**: Analyze survey responses, market reports, and customer interactions to identify trends, patterns, and sentiment insights.")
        st.write(" **Brand Reputation Management**: Monitor online mentions and discussions to assess brand sentiment and manage reputation effectively.")

        st.write("## How to Use This Application")

        st.write("Using our sentiment analysis application is simple and intuitive. You can upload text data, such as customer reviews, social media posts, or survey responses, and our application will analyze the sentiment expressed in the text. The results will be displayed visually, allowing you to gain valuable insights into the sentiment conveyed in your data.")

        st.write("## Get Started")

        st.write("Ready to explore the sentiment expressed in your text data? Head over to the sentiment analysis page and start analyzing text data with our powerful sentiment analysis tool!")

                

        st.write("This 'About' page provides users with an overview of sentiment analysis, its applications, and the functionality of the application. It aims to educate users about the significance of sentiment analysis and encourage them to explore the application further. Feel free to customize the content to fit the specific features and objectives of your sentiment analysis application.")
        st.write("If you have any questions or feedback, please visit our help page")
        