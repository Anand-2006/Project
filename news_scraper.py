from bs4 import BeautifulSoup
import requests

def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2')  # Modify based on website structure
    return [headline.text.strip() for headline in headlines]