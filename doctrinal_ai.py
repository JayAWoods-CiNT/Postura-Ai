import openai
import json

# Set up OpenAI API Key
openai.api_key = "YOUR-OPENAI-API-KEY-HERE"  # Replace with your actual OpenAI API key

# Load persona (doctrine and tone)
with open('persona.json', 'r') as file:
    persona = json.load(file)

def chat():
    while True:
        user_input = input("You: ")
        response = openai.ChatCompletion.create(  # Correct method
            model="gpt-3.5-turbo",  # Or gpt-4 if available
            messages=[
                {"role": "system", "content": persona['tone'] + " " + persona['behavior']},
                {"role": "user", "content": user_input}
            ]
        )
        print("AI: ", response['choices'][0]['message']['content'].strip())

if __name__ == "__main__":
    chat()
