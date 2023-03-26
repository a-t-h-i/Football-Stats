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


if not os.path.exisYts("token.json"):
    print("Whoops! Looks like you have not yet set up tour AI key.")
    print("You can get your open ai api key here: https://platform.openai.com/account/api-keys")
    key = input("Please enter your open ai key here: ")
    while not is_valid_key(key):
        print("The open ai key you entered is not valid.")
        key = input("Please enter your open ai key here: ")
    with open('token.json','w+') as file:
        json.dump({"ai_key":key},file)

with open('token.json','r') as file:
    data = json.load(file)
    openai.api_key = data["ai_key"]
