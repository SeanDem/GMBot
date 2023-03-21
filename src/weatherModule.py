from typing import List
import requests
import json
from people import Courtney, Lauren, Person, Sean, Laney, Kyle

class WeatherEngine:
    _baseUrl = 'https://api.weather.gov/points/'
    def __init__(self, person : Person):
        self.person = person
    
    def fetchWeather(self) -> list:
        response = requests.get(f'{self._baseUrl}{self.person.cords[0]},{self.person.cords[1]}')
        data = json.loads(response.text)
        forecastUrl = data['properties']['forecast']
        response = requests.get(forecastUrl)
        data = json.loads(response.text)

        forecasts = ["Todays Weather!\n"]
        for i in range(2):
            period = data['properties']['periods'][i]['name']
            detailed_forecast = data['properties']['periods'][i]['detailedForecast']
            forecasts.append(f'\n- {period}\'s forecast is {detailed_forecast}')
        
        self._weather = "".join(forecasts)
    
    @property
    def weather(self):
        return self._weather

