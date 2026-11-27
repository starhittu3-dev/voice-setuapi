
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from deep_translator import GoogleTranslator

app = FastAPI(
    title="Voice Setu API",
    description="AI Voice Translation API",
    version="1.0.0"
)

class TranslateRequest(BaseModel):
    text: str
    source_language: str = "auto"
    target_language: str = "en"

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
def translate(request: TranslateRequest):
    try:
        if not request.text.strip():
            raise HTTPException(
                status_code=400,
                detail="Text cannot be empty"
            )

        translator = GoogleTranslator(
            source=request.source_language,
            target=request.target_language
        )

        result = translator.translate(request.text)

        return {
            "status": "success",
            "original_text": request.text,
            "translated_text": result,
            "target_language": request.target_language
        }

    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
        
