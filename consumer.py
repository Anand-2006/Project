from kafka import KafkaConsumer
from sentiment_analysis import sentiment_analysis

def consume_messages(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092')
    for message in consumer:
        text = message.value.decode('utf-8')
        sentiment = sentiment_analysis(text)
        print(f"Processed Message: {text}, Sentiment: {sentiment}")