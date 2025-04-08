import base64
import os
import google.generativeai as genai
from prompt import prompt

def generate(query):
    
        api_key=os.environ.get("GEMINI_API_KEY")
        genai.configure(api_key=api_key)

        model1 = "gemini-2.0-flash"
        model = genai.GenerativeModel(model1)

        
        user_input = f"{prompt} to this {query}"
        response = model.generate_content(user_input)

        return response.text
        # print("Gemini:", response.text)



