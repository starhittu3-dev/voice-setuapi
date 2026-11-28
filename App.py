import FastAPI

app = FastAPI(
    title="Voice Setu API",
    description="Our own AI Voice Translation API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "app": "Voice Setu",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/api/translate")
def translate():
    return {
        "status": "pending",
        "message": "AI translation engine is not connected yet"
    }

