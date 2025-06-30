import json
from datetime import datetime

def save_feedback(question: str, response: str, rating: int = None):
    try:
        with open('feedback.json', 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"feedbacks": []}
    
    feedback = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "response": response,
        "rating": rating
    }
    
    data["feedbacks"].append(feedback)
    
    with open('feedback.json', 'w') as f:
        json.dump(data, f, indent=2)