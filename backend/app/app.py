from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from transformers import pipeline
from models.lang_model import generate_response

app = FastAPI()

# Define the database connection settings
db_config = {
    'user': 'your_user',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database',
}

# LLM setup (e.g., Hugging Face)
llm_pipeline = pipeline("text-generation", model="gpt-2")

class Query(BaseModel):
    user_query: str

def fetch_data_from_db(query: str):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result

@app.post("/query/")
async def query_product_supplier(query: Query):
    user_input = query.user_query
    
    # Generate a response using the LLM model
    llm_response = llm_pipeline(user_input)[0]['generated_text']
    
    # Example SQL query based on user input (you may need to parse this more effectively)
    sql_query = f"SELECT * FROM products WHERE product_name LIKE '%{user_input}%'"
    data = fetch_data_from_db(sql_query)
    
    # Summarize the database response using LLM
    summarized_data = llm_pipeline(f"Summarize this data: {data}")[0]['generated_text']
    
    return {"response": summarized_data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
