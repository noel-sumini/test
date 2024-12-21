from fastapi import FastAPI, Request
from fastapi import APIRouter
import uvicorn

app = FastAPI(
    title = "AI - FastAPI Application",
    description="AI",
    version = "0.0.1"
)
# app.include_router(main_router)

@app.get('/ping', status_code=200)
def health_check():
    return {"msg" : "pong"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port = 8000, reload = False)    