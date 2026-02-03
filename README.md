📧 Intelligent Email Classifier with LLM Explanations

An AI-powered email classification system that categorizes emails into Work, Personal, or Spam using transformer-based NLP models and provides human-readable explanations using Large Language Models (LLMs). The system is built with FastAPI and includes a feedback loop for continuous improvement.

🚀 Features

📌 Email classification using HuggingFace Transformer models

🤖 LLM-generated explanations for model predictions (OpenAI GPT)

⚡ FastAPI-based REST API

🔁 Feedback mechanism for improving model performance

📊 Confidence scores for each prediction

🧩 Modular, production-ready code structure

🧠 Tech Stack

Backend: FastAPI

NLP: HuggingFace Transformers (Zero-shot Classification)

LLM: OpenAI GPT API

Language: Python

Data Handling: JSON (feedback storage)

Deployment-ready: Docker-friendly structure

📁 Project Structure
email_classifier/
│
├── app/
│   ├── main.py            # FastAPI app
│   ├── classifier.py      # Email classification logic
│   ├── llm_explainer.py   # GPT-based explanation generator
│   ├── schemas.py         # Request/response models
│   └── feedback.py        # Feedback loop logic
│
├── data/
│   └── feedback.json      # Stores user corrections
│
├── requirements.txt
└── README.md

⚙️ Installation

Clone the repository

git clone https://github.com/AkashaMeh/intelligent-email-classifier.git
cd intelligent-email-classifier


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Set OpenAI API Key

export OPENAI_API_KEY="your_api_key_here"

▶️ Running the Application
uvicorn app.main:app --reload


Open API documentation:

http://127.0.0.1:8000/docs

📌 API Endpoints
🔹 Classify Email

POST /classify

Request

{
  "text": "Congratulations! You have won a free voucher."
}


Response

{
  "category": "spam",
  "confidence": 0.91,
  "explanation": "The email promotes a reward and urges immediate action, which is common in spam messages."
}

🔹 Submit Feedback

POST /feedback

Used to store corrected labels for future retraining.

🔁 Feedback Loop

Users can submit corrections if the predicted category is incorrect.
This feedback is stored and can later be used to:

Fine-tune supervised models

Improve prompt engineering

Analyze misclassification patterns

🧪 Future Improvements

Fine-tuned BERT model for supervised classification

Database integration (SQLite/PostgreSQL)

Docker + AWS deployment

LangChain-based explanation memory

Email ingestion via IMAP/SMTP

👩‍💻 Author

Akasha Mehmood
📎 GitHub: github.com/AkashaMeh

📎 LinkedIn: linkedin.com/in/akasha-mehmood