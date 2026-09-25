from google import genai
import os
from google.genai import types 
from dotenv import load_dotenv
import logging
from pydantic import BaseModel, Field
from typing import List, Optional

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

logging.getLogger("google_genai").setLevel(logging.ERROR)

client = genai.Client(api_key = api_key)

class job_postings(BaseModel):
    company: str = Field(description="Company name")
    role: str = Field(description="job title or role being hired for")
    skills: List[str] = Field(description="List of required Technical skills")
    experience: Optional[int] = Field(description="Minimum Experience requiered, if stated")
    location: Optional[str] = Field(description="location of the company, if stated")

def extract_job_postings(text: str) -> job_postings:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"Extract structured information from this job posting:\n\n{text}",
        config=types.GenerateContentConfig(
            temperature=0,
            response_mime_type="application/json",
            response_schema=job_postings
        )
    )
    return job_postings.model_validate_json(response.text)

if __name__ == "__main__":
    raw_text = input("Paste the job posting text:\n")
    result = extract_job_postings(raw_text)
    print(result.model_dump_json(indent=2))
