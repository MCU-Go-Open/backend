from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/PING")
def ping() -> str:
   return "PONG"

uvicorn.run(app, host='0.0.0.0', port=8080)
