from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filename, summary, clauses, risk_score, risk_level):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Lexora AI Report</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Executive Summary</b>", styles["Heading2"]))
    story.append(Paragraph(summary, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Risk Analysis</b>", styles["Heading2"]))
    story.append(
        Paragraph(
            f"Risk Score: {risk_score}/100 ({risk_level})",
            styles["BodyText"]
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Detected Clauses</b>", styles["Heading2"]))

    for clause in clauses:
        story.append(
            Paragraph(f"• {clause}", styles["BodyText"])
        )

    doc.build(story)