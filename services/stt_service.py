import os

class STTService:
    def __init__(self):
        # Whisper removed because it exceeds Render free-tier memory
        self.enabled = False

    def transcribe(self, file_path: str):
        """
        Speech-to-text is disabled on the free hosting plan
        because Whisper requires large memory.
        """

        try:
            if not os.path.exists(file_path):
                return None

            print("STT requested but Whisper is disabled due to memory limits.")

            return "Speech-to-text is currently disabled on this server."

        except Exception as e:
            print(f"Error during transcription: {e}")
            return None
