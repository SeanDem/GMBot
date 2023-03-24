import requests
from bs4 import BeautifulSoup

class NewsEngine:
    _url = "https://news.google.com/home?hl=en-US&gl=US&ceid=US:en"
    
    def _fetchNews(self) -> str:
        response = requests.get(self._url)
        soup = BeautifulSoup(response.content, 'html.parser')
        stories = soup.find_all('a', class_='WwrzSb')
        f = open("mocks/newsMock", "w")
        f.write(str(stories))
        f.close()
        news = []
        for i in range(len(stories)):
            news.append(f"{stories[i]['aria-label']}")
        return news
        
    def getNewsList(self):
        return self._fetchNews()
    
    def getNewsString(self):
        newsList = self._fetchNews()
        return "- " + "\n- ".join(newsList)
    
