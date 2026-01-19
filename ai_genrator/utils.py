from openai import OpenAI
from django.conf import settings
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY")
)


def generate_ai_description(product_name, material, color, audience, max_words):
    completion = client.chat.completions.create(
        model="google/gemma-3-27b-it:free",
        messages=[
            {
                "role": "user",
                "content": f"""
Generate ONLY 3 SEO-friendly product descriptions.

STRICT RULES:
- Each description MUST be under {max_words} words
- Total response should be concise
- No explanations
- No headings
- No SEO notes
- No questions
- Plain text only
- Separate each description with a newline

Product:
Name: {product_name}
Material: {material}
Color: {color}
Audience: {audience}
"""
            }
        ],
        extra_headers={
            "HTTP-Referer": settings.OPENROUTER_SITE_URL,
            "X-Title": settings.OPENROUTER_SITE_NAME,
        }
    )

    return completion.choices[0].message.content.strip()
