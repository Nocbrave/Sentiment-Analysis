import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self):
        self.data = []

    def fetch_data_from_api(self, api_url):
        # Fetch data from the specified API
        response = requests.get(api_url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Error fetching data from the API.")

    def scrape_data_from_website(self, url):
        # Scrape data from the specified website
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract relevant data from the webpage using BeautifulSoup
            # and add it to self.data list
            # Example: self.data = soup.find_all('p')
        else:
            print("Error scraping data from the website.")

    def analyze_sentiment(self):
        sentiment_scores = []
        for item in self.data:
            text = item['text']  # Extract text from the data

            # Perform sentiment analysis using TextBlob
            blob = TextBlob(text)
            sentiment_score = blob.sentiment.polarity
            sentiment_scores.append(sentiment_score)

            # Print sentiment analysis results
            print("Text:", text)
            print("Sentiment Score:", sentiment_score)
            print("-----------------")

        # Calculate overall sentiment score
        overall_sentiment_score = sum(sentiment_scores) / len(sentiment_scores)
        print("Overall Sentiment Score:", overall_sentiment_score)


# Example usage:

# Create an instance of SentimentAnalyzer
analyzer = SentimentAnalyzer()

# Fetch data from an API
api_url = "https://api.example.com/data"
analyzer.fetch_data_from_api(api_url)

# Scrape data from a website
website_url = "https://www.example.com"
analyzer.scrape_data_from_website(website_url)

# Analyze sentiment
analyzer.analyze_sentiment()
