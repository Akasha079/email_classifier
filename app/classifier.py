from transformers import pipeline

# Zero-shot classifier
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

LABELS = ["work", "personal", "spam"]

def classify_email(text: str):
    result = classifier(text, LABELS)
    label = result["labels"][0]
    score = float(result["scores"][0])
    return label, score
