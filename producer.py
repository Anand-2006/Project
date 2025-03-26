from kafka import KafkaProducer
from twitter_fetcher import fetch_twitter_data

def produce_messages(topic, hashtag):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    tweets = fetch_twitter_data(hashtag)
    for tweet in tweets:
        producer.send(topic, tweet['text'].encode('utf-8'))
    producer.close()