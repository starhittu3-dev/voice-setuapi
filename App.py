from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from deep_translator import GoogleTranslator

app = FastAPI(
    title="Voice Setu API",
    description="AI Voice Translation API",
    version="1.1.0"
)


class TranslateRequest(BaseModel):
    text: str
    source_lang: str = "hi"
    target_lang: str = "en"


@app.get("/")
def home():
    return {
        "app": "Voice Setu",
        "status": "running",
        "message": "Welcome to Voice Setu API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "api": "Voice Setu"
    }


@app.post("/api/translate")
def translate(request: TranslateRequest):

    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty"
        )

    try:
        translator = GoogleTranslator(
            source=request.source_lang,
            target=request.target_lang
        )

        translated_text = translator.translate(request.text)

        return {
            "status": "success",
            "app": "Voice Setu",
            "original_text": request.text,
            "translated_text": translated_text,
            "source_language": request.source_lang,
            "target_language": request.target_lang
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Translation failed: {str(error)}"
        )
        
