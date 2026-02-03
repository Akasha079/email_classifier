from pydantic import BaseModel

class EmailRequest(BaseModel):
    text: str

class EmailResponse(BaseModel):
    category: str
    confidence: float
    explanation: str

class FeedbackRequest(BaseModel):
    email_text: str
    predicted_category: str
    corrected_category: str
