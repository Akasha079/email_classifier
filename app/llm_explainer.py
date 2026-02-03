import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_explanation(email_text: str, label: str):
    prompt = f"""
You are an AI assistant.

Email:
"{email_text}"

Classification: {label}

Explain in 2-3 sentences why this email belongs to this category.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message["content"]
