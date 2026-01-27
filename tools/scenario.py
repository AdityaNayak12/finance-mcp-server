import pandas as pd

def scenario_simulation(csv_path, revenue_change_pct, expense_change_pct):
    df = pd.read_csv(csv_path)

    revenue = df[df["type"] == "income"]["amount"].sum()
    expenses = df[df["type"] == "expense"]["amount"].sum()

    revenue *= (1 + revenue_change_pct / 100)
    expenses *= (1 + expense_change_pct / 100)

    new_burn = expenses - revenue

    return {
        "adjusted_revenue": round(revenue, 2),
        "adjusted_expenses": round(expenses, 2),
        "new_burn_rate": round(new_burn, 2)
    }
