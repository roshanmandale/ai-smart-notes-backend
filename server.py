from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
from dotenv import load_dotenv

from services.extractor_service import ExtractorService
from services.ai_service import AIService

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

load_dotenv()

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="AI Smart Notes Backend")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

ai_service = AIService()
extractor_service = ExtractorService()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI Smart Notes Backend is running"}

@app.post("/summarize/youtube")
@limiter.limit("10/minute")
async def summarize_youtube(request: Request, url: str = Form(...)):
    video_id = extractor_service.get_video_id(url)
    transcript = extractor_service.extract_youtube_transcript(video_id)

    if not transcript:
        raise HTTPException(status_code=400, detail="Could not extract transcript")

    result = ai_service.generate_study_material(transcript)
    return result


@app.post("/summarize/pdf")
@limiter.limit("5/minute")
async def summarize_pdf(request: Request, file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extractor_service.extract_pdf_text(temp_path)
    os.remove(temp_path)

    if not text:
        raise HTTPException(status_code=400, detail="Could not extract text from PDF")

    result = ai_service.generate_study_material(text)
    return result


@app.post("/summarize/text")
@limiter.limit("10/minute")
async def summarize_text(request: Request, text: str = Form(...)):
    result = ai_service.generate_study_material(text)
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
