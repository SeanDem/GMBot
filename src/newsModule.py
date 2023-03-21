import requests
from bs4 import BeautifulSoup

# Define the URL of the news website you want to scrape


class NewsEngine:
    _url = "https://news.google.com/home?hl=en-US&gl=US&ceid=US:en"
    
    def __init__(self):
        pass
    
    def fetchNews(self) -> str:
        response = requests.get(self._url)
        soup = BeautifulSoup(response.content, 'html.parser')
        stories = soup.find_all('a', class_='WwrzSb')

        headlines = ["Todays News!\n"]
        for i in range(len(stories)):
            headlines.append(f"\n- {stories[i]['aria-label']}")
        self._news = "".join(headlines)
        
    @property 
    def news(self):
        return self._news