from backend.gemini_client import generate_response

def translate_text(text, language):
    prompt = f"""
You are an expert legal translator.

Translate ONLY the text below into {language}.

Rules:
- Do not summarize.
- Do not explain.
- Do not add or remove information.
- Preserve headings, lists, and formatting where possible.
- Return only the translated text.

Text:
{text}
"""

    return generate_response(prompt)