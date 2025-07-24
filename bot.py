import httpx

# Replace this with your OpenRouter API key
API_KEY = "your-api-key"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "your-gihub-account",  # Required, can be any personal site or GitHub
    "X-Title": "Command Line Chatbot"
}

def chatbot():
    print("Chatbot: Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        payload = {
            "model": "openai/gpt-3.5-turbo",  # You can change to other models too
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        try:
            response = httpx.post(BASE_URL, headers=HEADERS, json=payload)
            result = response.json()
            message = result["choices"][0]["message"]["content"]
            print("Chatbot:", message)

        except Exception as e:
            print("❌ Error:", e)

chatbot()
