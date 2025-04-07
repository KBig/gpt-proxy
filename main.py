from fastapi import FastAPI, Request
import httpx
import os

app = FastAPI()

# Ta clé OpenAI sera stockée dans une variable secrète Fly.io
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_URL = "https://api.openai.com/v1/chat/completions"

@app.post("/chat")
async def proxy_to_openai(req: Request):
    body = await req.json()
    
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(OPENAI_URL, headers=headers, json=body)
        return response.json()
