from backend.gemini_client import generate_response


def ask_question(document_text, question):

    prompt = f"""
You are LegalSaathi AI.

You are an experienced legal assistant.

Use the uploaded document as your PRIMARY source.

If the user asks:

• about information present in the document,
answer using the document.

If the user asks:

• why
• explain
• meaning
• legal implications
• legal risks

then explain using both:

1. the uploaded document
2. your legal knowledge

Always clearly distinguish between:

Information from the document.

General legal explanation.

Uploaded Document:

{document_text}

User Question:

{question}
"""

    return generate_response(prompt)