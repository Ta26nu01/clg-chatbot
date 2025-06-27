import requests

# URL of your Flask backend
url = "http://127.0.0.1:5000/chat"

# Example user message to send to the chatbot
data = {
    "message": "What are the required documents for B.Tech admission?"
}

try:
    response = requests.post(url, json=data)
    
    # Print the raw response (for debugging)
    print("🔁 Raw response text:", response.text)

    # Try to parse JSON and print the bot's response
    result = response.json()
    print("🤖 Bot says:", result["response"])

except requests.exceptions.RequestException as e:
    print("❌ Network error:", e)

except ValueError:
    print("❌ Couldn't decode JSON. Full response:\n", response.text)
