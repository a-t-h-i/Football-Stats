import openai

openai.api_key = "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"

def ask(query):
    
    completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=query,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,)

    response = completions.choices[0].text
    return response    
