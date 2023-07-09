# Sentiment-Analysis
A python project that uses natural language processing techniques to analyze social media or news sentiment related to cryptocurrencies.


Make sure you have the required libraries ```requests```, ```bs4```, ```textblob``` installed before running the code. You can install them using the following commands:
```
pip install requests
pip install beautifulsoup4
pip install textblob
```

__1. Data Retrieval:__

 - ```fetch_data_from_api``` method fetches data from a specified API using the ```requests``` library and stores it in the ```self.data``` list.
 - ```scrape_data_from_website``` method scrapes data from a specified website using the ```requests``` and ```BeautifulSoup``` libraries and stores it in the ```self.data``` list.
   
__2. Sentiment Analysis:__

 - ```analyze_sentiment``` method performs sentiment analysis on each item in the ```self.data``` list using the ```TextBlob``` library.
 - Sentiment scores are calculated for each item and stored in the ```sentiment_scores``` list.
 - The sentiment analysis results are printed for each item, and an overall sentiment score is calculated based on the average sentiment scores.
