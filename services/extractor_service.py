from youtube_transcript_api import YouTubeTranscriptApi
from pypdf import PdfReader
import os

class ExtractorService:
    @staticmethod
    def extract_youtube_transcript(video_id: str):
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            return " ".join([t['text'] for t in transcript_list])
        except Exception as e:
            print(f"Error fetching transcript: {e}")
            return None

    @staticmethod
    def extract_pdf_text(pdf_path: str):
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return None

    @staticmethod
    def get_video_id(url: str):
        if "v=" in url:
            return url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in url:
            return url.split("youtu.be/")[1].split("?")[0]
        return url
