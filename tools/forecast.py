import pandas as pd
import numpy as np

def forecast_financials(csv_path: str, months: int):
    df = pd.read_csv(csv_path)

    monthly = df.groupby(
        [df["date"].str[:7], "type"]
    )["amount"].sum().unstack().fillna(0)

    revenue_trend = np.polyfit(
        range(len(monthly)),
        monthly.get("income", 0),
        1
    )[0]

    forecast = []

    last = monthly.get("income", 0).iloc[-1]

    for i in range(months):
        last += revenue_trend
        forecast.append(round(float(last), 2))

    return {
        "months": months,
        "forecasted_revenue": forecast
    }
