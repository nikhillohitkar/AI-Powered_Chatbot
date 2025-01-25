from transformers import pipeline

def generate_response(query: str):
    model = pipeline("text-generation", model="gpt-2")
    response = model(query)
    return response[0]['generated_text']
