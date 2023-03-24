from datetime import date
import random

from people import Person


class PromptEngine:
    def getPromptBase(self, name):
        return f"""
    Write in the style of a close friend sending a text message. 
    Write a good morning message for your friend {name}. 
    I will provide information about for you to incorporate in your text 
    """
    
    def getTodaysDate(self):
        return f"""
    Todays date is {date.today().strftime('%A')} the {date.today().strftime('%-d')}th"""

    def getHoroscope(self, sign):
        return f"""
    Please include todays horoscope for {sign}. """
    
    def getFunFact(self):
        return f"""
    Please include a fun fact for your friend. """
    
    def getAffirmation(self):
        return f"""
    Please include an affirmation for your friend. """
    
    def getPoem(self):
        return f"""
    Please include a poem for your friend"""
    
    def getWeather(self, weatherStr):
        return f"""
    Here is todays weather for your friend. {weatherStr}."""
    
    def getNews(self, newsStr):
        return f"""
    Here is todays news for your friend. {newsStr}."""

    def getPrompt(self, person: Person):
        return f""" 
        {self.getPromptBase()}
        {self.getTodaysDate()}
        {self.getHoroscope()}
        {self.getAffirmation()}
        """.strip()

    def getPrompt(self, person: Person, weatherStr : str, newsStr: str):
       return f""" 
        {self.getPromptBase(person.name)}
        {self.getTodaysDate()}
        {self.getHoroscope(person.sign)}
        {self.getAffirmation()}
        {self.getNews(newsStr)}
        {self.getWeather(weatherStr)}
        """.strip()