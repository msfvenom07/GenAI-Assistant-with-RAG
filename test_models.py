import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print(f"Testing API key: {api_key[:10]}...")

# 1. Try listing models
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
try:
    response = requests.get(url)
    print(f"List Models Status: {response.status_code}")
    if response.status_code == 200:
        models = response.json().get("models", [])
        print("\nAvailable models:")
        for m in models:
            name = m.get("name")
            supported_methods = m.get("supportedGenerationMethods", [])
            if "embedContent" in supported_methods:
                print(f" - {name} (supports embedContent)")
            else:
                print(f" - {name}")
    else:
        print(f"Error listing models: {response.text}")
except Exception as e:
    print(f"Exception listing models: {e}")
