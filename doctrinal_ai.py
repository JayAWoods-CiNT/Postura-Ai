import openai
import json
import time

# Set up OpenAI API Key
openai.api_key = "YOUR-OPENAI-API-KEY-HERE"

# Load persona (doctrine and tone)
with open('persona.json', 'r') as file:
    persona = json.load(file)

def chat():
    while True:
        user_input = input("You: ")
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # You can change this to GPT-4 if available
            prompt=f"{persona['tone']} {persona['behavior']} {user_input}",
            max_tokens=150
        )
        print("AI: ", response.choices[0].text.strip())

if __name__ == "__main__":
    chat()

