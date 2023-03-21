import os
import random
import time
import schedule
from dotenv import load_dotenv
from people import Lauren, Person, Sean, Laney, Kyle
from textModule import TextEngine
from openAIModule import OpenAiEngine
from promptModule import PromptEngine
from weatherModule import WeatherEngine
from newsModule import NewsEngine

#########################
person: Person = Laney()
#########################    

def main():
    load_dotenv()
    rand = random.randint(400,600)/1000
    
    promptEngine = PromptEngine(person)
    openAiEngine = OpenAiEngine()
    textEngine = TextEngine()
    weatherEngine = WeatherEngine(person)
    newsEngine = NewsEngine()
    
    
    weatherEngine.fetchWeather()
    newsEngine.fetchNews()
    openAiEngine.generate(promptEngine.prompt, rand)
    
    
    print("here")
    text = f"""
    {openAiEngine.responseText}
    \n\n{weatherEngine.weather}
    \n\n{newsEngine.news}
    """
    textEngine.sendMessageTo(text, person.number)
    
    
    if bool(os.getenv("DEBUG")): 
        print(text)
   
# schedule.every().day.at("00:44").do(main)

# while True:
#     schedule.run_pending()
#     print("loop")
#     time.sleep(1)
    
main()