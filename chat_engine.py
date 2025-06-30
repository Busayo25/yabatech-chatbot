from transformers import pipeline
import json

# Initialize small model (choose one)
chatbot = pipeline(
    "text-generation",
    model="distilgpt2",  # Replace with your chosen model
    max_length=150,
    device="cpu"
)

with open('knowledge_base.json') as f:
    KNOWLEDGE = json.load(f)

def get_response(user_input: str) -> str:
    # 1. Check knowledge base first
    if "admission" in user_input.lower():
        return KNOWLEDGE["admissions"]["responses"][0]
    
    # 2. Use small transformer
    response = chatbot(
        f"Q: {user_input}\nA:",
        temperature=0.7,
        do_sample=True
    )[0]["generated_text"]
    
    return response.split("A:")[-1].strip()