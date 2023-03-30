import os
import random
import time
import schedule
from dotenv import load_dotenv
from people import Lauren, Person, PromptType, Sean, Laney, Kyle
from textModule import TwilioTextEngine
from openAiModule import OpenAiEngine
from promptModule import PromptEngine
from weatherModule import WeatherEngine
from newsModule import NewsEngine

#########################
person: Person = Laney()
#########################    

def main():
    load_dotenv()
    rand = random.randint(400,600)/1000
    
    openAiEngine = OpenAiEngine()
    twilioTextEngine = TwilioTextEngine()
    weatherEngine = WeatherEngine()
    newsEngine = NewsEngine()
    promptEngine =  PromptEngine()
    weatherStr = weatherEngine.getWeatherString(person.cords)
    newsStr = newsEngine.getNewsString()
    
    
    if person.promptType == PromptType.Full: 
        prompt = promptEngine.getPrompt(person, weatherStr, newsStr)
    else: 
        prompt = promptEngine.getPrompt(person)

    gptResponseStr = openAiEngine.getResponseText(prompt, rand)
    
    if person.promptType == PromptType.Full:
        text = f""" {gptResponseStr} """
    else: 
        text = f"""    
        {gptResponseStr}
        {newsStr}
        {weatherStr}
        """
        
    twilioTextEngine.sendMessageTo(text, person.number)
    
    if bool(os.getenv("DEBUG")): 
        print(text)

if __name__ == "__main__":
    main()