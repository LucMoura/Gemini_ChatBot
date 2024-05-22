# API da Banese com base na API do Gemini

# Para lançar o servidor você digita no terminal:
    uvicorn main:app --reload

# Caso não funcione digite:
    python -m uvicorn main:app --reload

# Após o servidor ter sido lançado, no postman coloque na URL:
    http://localhost:8000/chatbot

# Selecione o método POST, selencione o "raw" e digite a mensagem que quer testar em JSON (exemplo abaixo):
    {
    "mensagem": "commo faço para criar uma conta corrente?"
    }

