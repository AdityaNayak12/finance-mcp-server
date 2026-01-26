import pandas as pd

def compute_kpis(csv_path: str):
    df = pd.read_csv(csv_path)

    revenue = df[df["type"] == "income"]["amount"].sum()
    expenses = df[df["type"] == "expense"]["amount"].sum()

    burn_rate = expenses - revenue
    monthly_burn = burn_rate / max(df["date"].nunique(), 1)

    cash_balance = revenue - expenses
    runway = None

    if monthly_burn > 0:
        runway = cash_balance / monthly_burn

    return {
        "total_revenue": revenue,
        "total_expenses": expenses,
        "monthly_burn": round(monthly_burn, 2),
        "cash_balance": round(cash_balance, 2),
        "runway_months": round(runway, 2) if runway else "Infinite"
    }
