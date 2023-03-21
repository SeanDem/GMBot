import os
import openai

class OpenAiEngine:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def generate(self, prompt: str, temp: int):
        self.response = openai.Completion.create(
            model="text-davinci-003", 
            prompt=prompt, 
            temperature= temp, 
            max_tokens=800)
   
    @property  
    def responseText(self):
        return self.response['choices'][0]['text']

