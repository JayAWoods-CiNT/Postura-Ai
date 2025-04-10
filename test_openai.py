import openai

openai.api_key = "YOUR-OPENAI-API-KEY-HERE"  # Replace with your actual OpenAI API key

response = openai.chat_completions.create(
    model="gpt-3.5-turbo",  # Or gpt-4 if available
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello to Termux!"}
    ]
)

print(response)
