
from fastapi import FastAPI, UploadFile, File

app = FastAPI(
    title="Voice Setu API",
    description="AI Voice Translation API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "healthy",
        "message": "Welcome to Voice Setu API"
    }

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "Audio received successfully"
    }
  
