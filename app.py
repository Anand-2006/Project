from flask import Flask, jsonify
from twitter_fetcher import fetch_twitter_data
from news_scraper import scrape_news
from sentiment_analysis import sentiment_analysis

app = Flask(__name__)

@app.route('/api/disaster-data', methods=['GET'])
def get_disaster_data():
    # Fetch data from Twitter and News
    tweets = fetch_twitter_data("#disaster")
    news_data = scrape_news("https://newswebsite.com/disaster-news")

    # Process data using sentiment analysis
    processed_tweets = [{"text": tweet['text'], "sentiment": sentiment_analysis(tweet['text'])} for tweet in tweets]
    processed_news = [{"headline": news, "sentiment": sentiment_analysis(news)} for news in news_data]

    # Combine and return processed data
    combined_data = {
        "tweets": processed_tweets,
        "news": processed_news
    }
    return jsonify(combined_data)

if __name__ == '__main__':
    app.run(debug=True)