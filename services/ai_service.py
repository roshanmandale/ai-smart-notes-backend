import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

class AIService:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.getenv("NVIDIA_API_KEY")
        )

    def generate_study_material(self, content: str):
        prompt = f"""
        Analyze the following lecture content and generate:
        1. Short summary
        2. Key bullet points
        3. Important concepts
        4. Flashcards (Question and Answer format)
        5. Quiz questions (MCQ format with options and correct answer)
        6. Revision notes

        Return the result in the following structured JSON format:
        {{
            "summary": "",
            "key_points": [],
            "concepts": [],
            "flashcards": [
                {{"question": "", "answer": ""}}
            ],
            "quiz": [
                {{"question": "", "options": ["A", "B", "C", "D"], "answer": "X"}}
            ],
            "revision_notes": ""
        }}

        Content:
        {content[:10000]}  # Limit content to 10k characters for stability
        """

        response = self.client.chat.completions.create(
            model="meta/llama-3.1-405b-instruct", # Using a highly capable NVIDIA model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            top_p=1,
            max_tokens=2048,
            response_format={"type": "json_object"}
        )

        try:
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"Error parsing AI response: {e}")
            return None
