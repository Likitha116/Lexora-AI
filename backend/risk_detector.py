RISK_POINTS = {
    "Non-Compete": 30,
    "Liability": 25,
    "Confidentiality": 10,
    "Arbitration": 10,
    "Termination": 10,
    "Salary": 0,
    "Working Hours": 0,
    "Leave Policy": 0
}


def calculate_risk(clauses):
    score = 0

    for clause in clauses:
        score += RISK_POINTS.get(clause, 0)

    if score <= 30:
        level = "🟢 Low"

    elif score <= 60:
        level = "🟡 Medium"

    else:
        level = "🔴 High"

    return score, level