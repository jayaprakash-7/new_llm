from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def landing_page():
    return {
        "message" : "Hi Hello"
    }

@app.get("/health")
def health():
    return {
        "message" : "Your Health is good"
    }
    