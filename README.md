# Structured Extraction CLI

Extracts structured JSON data (company, role, required skills, experience, location) from unstructured job posting text, using the Gemini API's structured output feature (JSON schema enforcement via Pydantic).

## Why this exists
Free-text LLM output is unreliable to parse. This forces the model to return data matching a strict schema, so the output is guaranteed valid and typed — no regex hacking, no hoping the JSON parses.

## Setup

```bash
pip install -U google-genai pydantic
export GEMINI_API_KEY="your-api-key-here"
```

## Usage

```bash
python extract.py
```

Paste job posting text when prompted. Returns structured JSON like:

```json
{
  "company": "Nimbus Cloud Technologies",
  "role": "Software Engineer - Backend",
  "required_skills": ["Python", "Go", "REST API design", "PostgreSQL", "Docker"],
  "experience_years": 2,
  "location": "Bangalore, India"
}
```

## Stack
- Google Gemini API (`google-genai` SDK)
- Pydantic for schema definition and validation
