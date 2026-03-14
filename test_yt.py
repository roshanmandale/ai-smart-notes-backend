try:
    print("Importing YouTubeTranscriptApi...")
    from youtube_transcript_api import YouTubeTranscriptApi
    print("Success!")
except Exception as e:
    print(f"FAILED: {e}")
    import traceback
    traceback.print_exc()
