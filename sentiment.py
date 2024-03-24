import streamlit as st
import pandas as pd
from textblob import TextBlob
import plotly.graph_objects as go  # Import Plotly graph objects
from recommendations import *


# Function for sentiment analysis
def analyze_sentiment(review):
    analysis = TextBlob(str(review))
    return analysis.sentiment.polarity

def classify_sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

# Landing page function
def sentiment(c=None):
    st.title('Sentiment Analysis Landing Page')
    st.write("This sentiment results are based on amazon reviews provide by the dataset in amazon.csv uploaded a while back.")
    
    # Your code for sentiment analysis on amazon.csv goes here
    df = pd.read_csv("amazon.csv")

    # Perform sentiment analysis on the review text
    df['sentiment_score'] = df['reviewText'].apply(analyze_sentiment)
    df['sentiment'] = df['sentiment_score'].apply(classify_sentiment)

    # Display sentiment analysis results
    st.write("### Sentiment Analysis Results:")
    st.write(df[['reviewText', 'sentiment', 'sentiment_score']])

    # Display sentiment distribution using pie chart
    st.write("### Sentiment Distribution (Pie Chart):")
    sentiment_counts = df["sentiment"].value_counts()
    fig1 = go.Figure(data=[go.Pie(labels=sentiment_counts.index, values=sentiment_counts)])
    st.plotly_chart(fig1)

    # Display sentiment scores distribution using bar graph
    st.write("### Sentiment Scores Distribution (Bar Graph):")
    column_name = 'sentiment'  # Change this to the column containing sentiment scores
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Specify your desired colors
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=df[column_name].value_counts().values.tolist(),
        x=[str(i) for i in df[column_name].value_counts().index],
        text=df[column_name].value_counts().values.tolist(),
        name=column_name,
        textposition='auto',
        showlegend=False,
        marker=dict(color=colors)))
    st.plotly_chart(fig)
    if st.button("View Recommendations"):
        recommendations()

if __name__ == '__main__':
    sentiment()
