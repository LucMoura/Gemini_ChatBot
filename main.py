from fastapi import FastAPI, Request
from app import *  
app = FastAPI()

@app.post("/chatbot")
async def conversar(request: Request):
    request_data = await request.json()  
    question = request_data["mensagem"]  
    response = chat.send_message(question)  
    return {"resposta": response.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
