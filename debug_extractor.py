try:
    print("Importing youtube_transcript_api...")
    from youtube_transcript_api import YouTubeTranscriptApi
    print("Importing fitz (PyMuPDF)...")
    import fitz
    print("Importing os...")
    import os
    print("All extractor imports successful!")
except Exception as e:
    print(f"FAILED: {e}")
    import traceback
    traceback.print_exc()
