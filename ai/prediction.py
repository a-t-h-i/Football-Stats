import openai
import os
#You can get your open ai api key here: https://platform.openai.com/account/api-keys
openai.api_key = ""

def ask(query):
    
    completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=query,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,)

    response = completions.choices[0].text
    return response    