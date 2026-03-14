try:
    print("Importing fitz...")
    import fitz
    print("Success!")
except Exception as e:
    print(f"FAILED: {e}")
    import traceback
    traceback.print_exc()
