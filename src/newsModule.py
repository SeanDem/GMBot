import requests
from bs4 import BeautifulSoup

# Define the URL of the news website you want to scrape


class NewsSingleton:
    _url = "https://news.google.com/home?hl=en-US&gl=US&ceid=US:en"
    
    def fetchNews(self) -> str:
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
        return self.fetchNews()
    
    def getNewsString(self):
        newsList = self.fetchNews()
        return "- " + "\n- ".join(newsList)
    
