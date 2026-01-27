import pandas as pd

def compute_vc_metrics(csv_path):
    df = pd.read_csv(csv_path)

    revenue = df[df["type"] == "income"]["amount"].sum()
    expenses = df[df["type"] == "expense"]["amount"].sum()

    burn_multiple = expenses / max(revenue, 1)

    return {
        "burn_multiple": round(burn_multiple, 2),
        "capital_efficiency": round(revenue / max(expenses, 1), 2)
    }


def investment_readiness_score(csv_path):
    metrics = compute_vc_metrics(csv_path)

    score = 0
    if metrics["burn_multiple"] < 2:
        score += 40
    if metrics["capital_efficiency"] > 1:
        score += 40
    score += 20

    return {
        "investment_readiness_score": score,
        "interpretation": (
            "Strong" if score >= 80 else
            "Moderate" if score >= 50 else
            "Weak"
        )
    }
