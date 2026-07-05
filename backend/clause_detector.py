CLAUSES = {
    "Salary": ["salary", "compensation"],
    "Termination": ["termination", "terminate"],
    "Confidentiality": ["confidential"],
    "Non-Compete": ["non-compete", "competing company"],
    "Liability": ["liability", "damages"],
    "Arbitration": ["arbitration"],
    "Leave Policy": ["leave"],
    "Working Hours": ["working hours"]
}

def detect_clauses(text):
    found = []

    text = text.lower()

    for clause, keywords in CLAUSES.items():
        for keyword in keywords:
            if keyword.lower() in text:
                found.append(clause)
                break

    return found