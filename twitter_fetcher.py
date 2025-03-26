import requests

def fetch_twitter_data(hashtag):
    url = f"https://api.twitter.com/2/tweets/search/recent?query={hashtag}&tweet.fields=geo"
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print("Error fetching Twitter data:", response.status_code)
        return []