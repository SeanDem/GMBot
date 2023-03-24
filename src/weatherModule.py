from typing import List
import requests
import json
from people import Courtney, Lauren, Person, Sean, Laney, Kyle

class WeatherEngine:
    _baseUrl = 'https://api.weather.gov/points/'
    
    def fetchWeather(self, cords: tuple) -> list:
        response = requests.get(f'{self._baseUrl}{cords[0]},{cords[1]}')
        data = json.loads(response.text)
        forecastUrl = data['properties']['forecast']
        response = requests.get(forecastUrl)
        data = json.loads(response.text)
        return data
    
    def getWeatherList(self, cords: tuple) -> List[str]:
        data  = self.fetchWeather(cords)
        weatherList = []
        for i in range(2):
            period = data['properties']['periods'][i]['name']
            detailedForecast = data['properties']['periods'][i]['detailedForecast']
            weatherList.append(f'{period}\'s forecast is {detailedForecast}')
        return weatherList

    def getWeatherString(self, cords) -> str:
        weatherList  = self.getWeatherList(cords)
        return "- " + "\n- ".join(weatherList)
        