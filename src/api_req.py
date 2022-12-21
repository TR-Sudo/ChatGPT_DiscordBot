import os
import openai
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

def res(userPrompt):
    openai.organization = os.getenv("ORG_ID")
    openai.api_key=os.getenv("API_KEY")

    #makes request with required parameters
    res=openai.Completion.create(
        model='text-davinci-003',
        prompt=userPrompt,
        max_tokens=2000,
        temperature=0.6
    )
    
    #returns only text response
    return  (res['choices'][0]['text'])