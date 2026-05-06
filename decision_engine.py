import requests
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_food_recommendation(context, user_input):
    prompt = f"""
You are a smart food assistant.

User said: {user_input}

Context:
Time: {context['time']}
Goal: {context['goal']}
Last meal: {context['last_meal']}

Give:
1. Two food suggestions
2. Why they are good choices
Keep it short and practical.
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

    response = requests.post(
        url,
        json={
            "contents": [{"parts": [{"text": prompt}]}]
        }
    )

    try:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        return "Error getting recommendation."