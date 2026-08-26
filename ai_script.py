import os
import requests

api_key = os.environ.get("GOROUTER_API_KEY")

url = "https://api.gorouter.app/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://gorouter.app",
    "Referer": "https://gorouter.app/"
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

session = requests.Session()
response = session.post(url, headers=headers, json=data, timeout=60)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    result = response.json()
    ai_reply = result['choices'][0]['message']['content']
    print(f"✅ AI Response: {ai_reply}")
else:
    print(f"❌ Error {response.status_code}: {response.text[:500]}")
