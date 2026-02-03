from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.schemas import EmailRequest, EmailResponse, FeedbackRequest
from app.classifier import classify_email
from app.llm_explainer import generate_explanation
from app.feedback import save_feedback

app = FastAPI(title="Intelligent Email Classifier")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('app/static/index.html')

@app.post("/classify", response_model=EmailResponse)
def classify_email_api(request: EmailRequest):
    label, confidence = classify_email(request.text)
    explanation = generate_explanation(request.text, label, request.llm_provider)

    return {
        "category": label,
        "confidence": confidence,
        "explanation": explanation
    }

@app.post("/feedback")
def feedback(request: FeedbackRequest):
    save_feedback(request.email_text, request.predicted_category, request.corrected_category)
    return {"message": "Feedback saved successfully"}
