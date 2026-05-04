import json
import os

from dotenv import load_dotenv
from openai import OpenAI
from fastapi import HTTPException

load_dotenv(override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
GROQ_BASE_URL = "https://api.groq.com/openai/v1"


def _get_client() -> OpenAI:
    # Re-read env var at call time
    load_dotenv(override=True)
    api_key = os.getenv("GROQ_API_KEY", "")
    if not api_key or api_key == "your-groq-api-key-here":
        raise HTTPException(
            status_code=503,
            detail="Groq API key not configured. Set GROQ_API_KEY in .env",
        )
    return OpenAI(base_url=GROQ_BASE_URL, api_key=api_key)


def generate_ai_roadmap(target_role: str, missing_skills: list[str]) -> dict:
    client = _get_client()
    # Re-read model at call time so .env changes are picked up on reload
    load_dotenv(override=True)
    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    skills_str = ", ".join(missing_skills)
    prompt = f"""You are a career development expert. Generate a learning roadmap for someone targeting the role of "{target_role}" who is missing the following skills: {skills_str}.

For each missing skill, provide:
- The skill name
- A list of 3-5 concrete learning steps (actionable, specific)
- Estimated time to learn (e.g., "2 weeks", "1 month")

Respond ONLY with valid JSON in this exact format, no other text:
{{
  "roadmap": [
    {{
      "skill": "skill name",
      "learning_steps": ["step 1", "step 2", "step 3"],
      "estimated_time": "X weeks"
    }}
  ]
}}"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that only responds with valid JSON."},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
        temperature=0.7,
        max_tokens=2048,
    )

    content = response.choices[0].message.content
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=502,
            detail="AI returned invalid JSON response",
        )
