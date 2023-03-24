import os
import random
import time
import schedule
from dotenv import load_dotenv
from people import Lauren, Person, Sean, Laney, Kyle
from textModule import TwilioTextEngine
from openAiModule import OpenAiEngine
from promptModule import PromptEngine
from weatherModule import WeatherEngine
from newsModule import NewsEngine

#########################
person: Person = Sean()
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
    
    
    if person.prompt == "full":
        prompt = promptEngine.fullPrompt
    else: prompt = promptEngine.halfPrompt

    gptResponseStr = openAiEngine.getResponseText(prompt, rand)
    
    if person.prompt == "full":
        text = f""" {gptResponseStr} """
    else: 
        text = f"""    
        {gptResponseStr}
        {newsStr}
        {weatherStr}
        """
        
    twilioTextEngine.sendMessageTo(text, person.number)
    
    if bool(os.getenv("DEBUG")): 
        print()
   
# schedule.every().day.at("11:15").do(main)

# while True:
#     schedule.run_pending()
#     time.sleep(10)

main()