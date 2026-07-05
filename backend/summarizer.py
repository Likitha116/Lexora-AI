from backend.gemini_client import generate_response


def summarize_document(text):

    prompt = f"""
You are an expert legal advisor.

Analyze the following legal document professionally.

DOCUMENT:

{text}

Return the answer in Markdown.

Use these headings exactly.

# Executive Summary

Summarize the document in 5-8 points.

# Risk Analysis

Mention all risks.

Classify each as:

🟢 Low

🟡 Medium

🔴 High

Explain why.

# Important Clauses

List every important clause.

# Financial Commitments

Mention payments, penalties, liabilities or compensation.

If none exists, say "None found."

# Important Dates

Mention all dates and deadlines.

If none exists, say "None found."

# Plain English

Explain the document like you're explaining it to a 15-year-old.

# Questions You Should Ask

Suggest questions the user should ask before signing this document.
"""

    return generate_response(prompt)