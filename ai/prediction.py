"""GOOGLE GEMINI API"""
import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("MY_KEY"))

def ask(query):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    return model.generate_content(query).candidates[0].content.parts[0].text