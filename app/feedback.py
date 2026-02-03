import json
from datetime import datetime

FEEDBACK_FILE = "data/feedback.json"

def save_feedback(email_text, predicted, corrected):
    feedback = {
        "email": email_text,
        "predicted": predicted,
        "corrected": corrected,
        "timestamp": str(datetime.now())
    }

    try:
        with open(FEEDBACK_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(feedback)

    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=2)
