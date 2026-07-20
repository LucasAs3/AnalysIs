from dotenv import load_dotenv
from google import genai
import json
import os
from Functions.Ai.prompts import DOCUMENT_ANALYSIS_PROMPT

load_dotenv()

API_KEY = os.getenv("API_KEY_GEMINI")

client = genai.Client(api_key=API_KEY)

def do_a_document_analyze(doc: str) -> str:
    prompt = DOCUMENT_ANALYSIS_PROMPT.format(text=doc)

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return json.loads(response.text)

