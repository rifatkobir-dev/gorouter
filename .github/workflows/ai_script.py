import os
import requests
import json

api_key = os.environ.get("GOROUTER_API_KEY")

url = "https://gorouter.app/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model": "claude-opus-5-thinking",
    "messages": [
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ]
}

print("🤖 AI কে request পাঠানো হচ্ছে...")

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    ai_reply = result['choices'][0]['message']['content']
    print(f"✅ AI Response: {ai_reply}")
else:
    print(f"❌ Error {response.status_code}: {response.text}")
