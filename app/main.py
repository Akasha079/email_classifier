from fastapi import FastAPI
from app.schemas import EmailRequest, EmailResponse
from app.classifier import classify_email
from app.llm_explainer import generate_explanation
from app.feedback import save_feedback

app = FastAPI(title="Intelligent Email Classifier")

@app.post("/classify", response_model=EmailResponse)
def classify_email_api(request: EmailRequest):
    label, confidence = classify_email(request.text)
    explanation = generate_explanation(request.text, label)

    return {
        "category": label,
        "confidence": confidence,
        "explanation": explanation
    }

@app.post("/feedback")
def feedback(email: str, predicted: str, corrected: str):
    save_feedback(email, predicted, corrected)
    return {"message": "Feedback saved successfully"}
