from pydantic import BaseModel

class EmailRequest(BaseModel):
    text: str

class EmailResponse(BaseModel):
    category: str
    confidence: float
    explanation: str
