try:
    print("Importing os...")
    import os
    print("Importing fastapi...")
    from fastapi import FastAPI
    print("Importing services.extractor_service...")
    from services.extractor_service import ExtractorService
    print("Importing services.ai_service...")
    from services.ai_service import AIService
    print("Importing services.stt_service...")
    from services.stt_service import STTService
    print("All imports successful!")
except Exception as e:
    print(f"FAILED: {e}")
    import traceback
    traceback.print_exc()
