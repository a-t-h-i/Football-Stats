import openai
import os



openai.api_key = os.environ.get("MY_KEY")


def ask(query):
    
    completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=query,
    max_tokens=512,
    n=1,
    stop=None,
    temperature=0.6,)

    response = completions.choices[0].text
    return response
