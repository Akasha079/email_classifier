# 📧 Intelligent Email Classifier with LLM Explanations

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-green)
![OpenAI](https://img.shields.io/badge/AI-OpenAI-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

An AI-powered email classification system that categorizes emails into **Work**, **Personal**, or **Spam** using transformer-based NLP models and provides human-readable explanations using Large Language Models (LLMs). The system is built with **FastAPI** and includes a feedback loop for continuous improvement.

---

## 🚀 Features

- 📌 **Email Classification**: Uses HuggingFace Transformer models for zero-shot classification.
- 🤖 **LLM Explanations**: Generates human-readable explanations for predictions using OpenAI/Groq keys.
- ⚡ **FastAPI Interface**: High-performance REST API.
- 🔁 **Feedback Loop**: Mechanism to collect user corrections for future retraining.
- 📊 **Confidence Scores**: Returns confidence levels for each prediction.
- 🧩 **Modular Design**: Production-ready, organized code structure.

## 🧠 Tech Stack

| Component | Technology | Description |
|-----------|------------|-------------|
| **Backend** | API | FastAPI |
| **NLP** | Model | HuggingFace Transformers (Zero-shot) |
| **LLM** | Explainer | OpenAI GPT / Google Gemini |
| **Language** | Runtime | Python |
| **Data** | Storage | JSON (Feedback storage) |

## 📁 Project Structure

```bash
email_classifier/
│
├── app/
│   ├── main.py            # FastAPI app entry point
│   ├── classifier.py      # Core email classification logic
│   ├── llm_explainer.py   # GPT-based explanation generator
│   ├── schemas.py         # Pydantic models for Request/Response
│   └── feedback.py        # Feedback loop management
│
├── data/
│   └── feedback.json      # Storage for user corrections
│
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/AkashaMeh/intelligent-email-classifier.git
cd intelligent-email-classifier
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure LLM Provider (OpenAI / Gemini)
You can switch between OpenAI and Google Gemini by setting the `LLM_PROVIDER` environment variable.

#### Option A: OpenAI (Default)
```bash
export OPENAI_API_KEY="your_openai_key"
export LLM_PROVIDER="openai"
```

#### Option B: Google Gemini
```bash
export GEMINI_API_KEY="your_gemini_key"
export LLM_PROVIDER="gemini"
```

## ▶️ Running the Application

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at:
- **Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) -- Interactive Swagger UI
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) -- ReDoc documentation

## 📌 API Endpoints

### 🔹 Classify Email
**POST** `/classify`

Analyzes the email content and returns a category with an explanation.

**Request Body:**
```json
{
  "text": "Congratulations! You have won a free voucher."
}
```

**Response:**
```json
{
  "category": "spam",
  "confidence": 0.91,
  "explanation": "The email promotes a reward and urges immediate action, which is common in spam messages."
}
```

### 🔹 Submit Feedback
**POST** `/feedback`

Used to store corrected labels for future retraining.

**Query Parameters:**
- `email`: The content of the email.
- `predicted`: The category predicted by the model.
- `corrected`: The correct category provided by the user.

**Example Request:**
```bash
POST /feedback?email=Hello&predicted=spam&corrected=personal
```

## 🔁 Feedback Loop
Users can submit corrections if the predicted category is incorrect. This feedback is stored in `data/feedback.json` and can be used to:
- Fine-tune supervised models.
- Improve prompt engineering.
- Analyze misclassification patterns.

## 🧪 Future Improvements
- [ ] Fine-tune BERT model for supervised classification.
- [ ] Database integration (SQLite/PostgreSQL) instead of JSON.
- [ ] Docker + AWS deployment support.
- [ ] LangChain-based explanation memory.
- [ ] Email ingestion via IMAP/SMTP.

## 👩‍💻 Author

**Akasha Mehmood**

- 📎 **GitHub**: [github.com/AkashaMeh](https://github.com/AkashaMeh)
- 📎 **LinkedIn**: [linkedin.com/in/akasha-mehmood](https://linkedin.com/in/akasha-mehmood)