import whisper
import os

class STTService:
    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self, file_path: str):
        try:
            result = self.model.transcribe(file_path)
            return result["text"]
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return None
