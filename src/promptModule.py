from datetime import date
import random

from people import Person


class PromptEngine:
    def __init__(self, person : Person, weather: str, news: str):
        self.news = news
        self.weather = weather
        self.person = person
        self.LOW_RAND = 10
        self.HIGH_RAND = 10
    
    @property 
    def prompt(self):
       return f""" 
        {self.gmBase}
        {self.todaysDate}
        {self.horoscope}
        {self.affirmation}
        """.strip()

    @property
    def gmBase(self):
        return f"Write in the style of a close friend sending a text message. Write a good morning message for your friend {self.person.name}? "
    
    @property
    def todaysDate(self):
        return f"Todays date is {date.today().strftime('%A')} the {date.today().strftime('%-d')}th" if self.randomizer(self.HIGH_RAND) else ''
      
    @property
    def traits(self):
        return f"My friend has the following personality traits use these to help understand my friend but not add them directly to the message. : {', '.join(map(str, self.person.traits))}. Use these to help generate a but do not include these in output. "
    
    @property
    def interests(self):
        return f"My friend has the following interests use these to help understand my friend but not add them directly to the message. : {', '.join(map(str, self.person.interests))}. Use these to help generate a but do not include these in output. "
    
    @property
    def horoscope(self):
        return f"In a new paragraph, Please include todays horoscope for {self.person.sign}. " if self.randomizer(self.HIGH_RAND) else ''
    
    @property
    def funFact(self):
        return f"In a new paragraph, Please include aa fun fact that would interest my friend. " if self.randomizer(self.LOW_RAND) else ''
    
    @property
    def affirmation(self):
        return f"In a new paragraph, Please include an affirmation for my friend. " if self.randomizer(self.LOW_RAND) else ''
    
    @property
    def poem(self):
        return f"In a new paragraph. Please include a poem for my friend"
    
    @property
    def weather(self):
        return f"In a new paragraph. Please format todays weather weather properly. Here is todays weather {self.weather}."
    
    @property
    def weather(self):
        return f"In a new paragraph. Please format todays new headlines properly. Here is are some todays headlines {self.news}."

    
    def randomizer(self, percent = 5):
        return random.randint(0,10) <= percent
            
      
