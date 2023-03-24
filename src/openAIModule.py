import os
import openai

class OpenAiEngine:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def _generate(self, prompt: str, temp: int):
        response = openai.Completion.create(
            model="text-davinci-003", 
            prompt=prompt, 
            temperature= temp, 
            max_tokens=1000)
        return response
   
    def getResponseText(self, prompt: str, temp: int) -> str:
        """Call chatGPT api with prompt and temp extract and return response text 

        Args:
            prompt (str): prompt for ChatGPT to generate
            temp (int): chatGPT temp setting, how random to make response

        Returns:
            _type_: response text
        """        
        return self._generate(prompt, temp)['choices'][0]['text']

