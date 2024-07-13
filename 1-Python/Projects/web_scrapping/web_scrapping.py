import requests
from bs4 import BeautifulSoup

# Example function to scrape quotes from http://quotes.toscrape.com/
def scrape_quotes():
    url = 'http://quotes.toscrape.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.select('.quote span.text')
        
        for quote in quotes:
            print(quote.text)
    else:
        print(f"Error fetching {url}: {response.status_code}")

scrape_quotes()
