from fastapi import FastAPI

app = FastAPI(title="job board", version="0.1.0")

@app.get("/")
def hello_api():
    return "testing"