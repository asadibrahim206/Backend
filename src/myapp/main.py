from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok", "version": "0.1.0"}

@app.get("/")
def root():
    return {"message": "myapp API is running. See /docs for the API docs."}