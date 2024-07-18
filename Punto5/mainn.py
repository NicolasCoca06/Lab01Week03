from fastapi import FastAPI
import uvicorn
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

def summarize_text(text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Please summarize the following text in less than 100 words: " + text)
    return response.text


from vertexai.preview import tokenization
def count_tokens(text):
    model_name = "gemini-1.5-flash-001"
    tokenizer = tokenization.get_tokenizer_for_model(model_name)

    result = tokenizer.count_tokens(text)

    return result

print(count_tokens("Hello, world!"))    

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Worldddd"}

@app.post("/summarize/")
async def summarize(input: str):
    
    summary = summarize_text(input)
    return {"summary": summary}

@app.post("/count_tokens/")
async def count(input: str):
    
    token_count = count_tokens(input)
    return {"token_count": token_count}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
