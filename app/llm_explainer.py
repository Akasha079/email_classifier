import openai
import os
import google.generativeai as genai

# Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()

if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def generate_explanation(email_text: str, label: str, provider: str = None):
    prompt = f"""
You are an AI assistant.

Email:
"{email_text}"

Classification: {label}

Explain in 2-3 sentences why this email belongs to this category.
"""
    
    # Use passed provider if explicit, otherwise fallback to env
    selected_provider = provider.lower() if provider else LLM_PROVIDER
    
    if selected_provider == "gemini":
        return generate_gemini_explanation(prompt)
    else:
        return generate_openai_explanation(prompt)

def generate_openai_explanation(prompt: str):
    if not OPENAI_API_KEY:
        return "Error: OPENAI_API_KEY not found."

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"OpenAI Error: {str(e)}"

def generate_gemini_explanation(prompt: str):
    if not GEMINI_API_KEY:
        return "Error: GEMINI_API_KEY not found."

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini Error: {str(e)}"
