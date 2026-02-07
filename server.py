from mcp.server.fastmcp import FastMCP

from tools.loader import load_data
from tools.kpis import compute_kpis
from tools.forecast import forecast_financials
from tools.scenario import scenario_simulation
from tools.vc_metrics import compute_vc_metrics, investment_readiness_score

mcp = FastMCP("finance-mcp")


@mcp.tool()
def load_financial_data(csv_path: str) -> dict:
    return load_data(csv_path)

@mcp.tool()
def compute_financial_kpis(csv_path: str) -> dict:
    return compute_kpis(csv_path)

@mcp.tool()
def forecast(csv_path: str, months: int = 6) -> dict:
    return forecast_financials(csv_path, months)

@mcp.tool()
def scenario_simulation_mcp(
    csv_path: str,
    revenue_change_pct: float = 0,
    expense_change_pct: float = 0
) -> dict:
    return scenario_simulation(csv_path, revenue_change_pct, expense_change_pct)

@mcp.tool()
def compute_vc_metrics(csv_path: str) -> dict:
    return compute_vc_metrics(csv_path)

@mcp.tool()
def investment_readiness(csv_path: str) -> dict:
    return investment_readiness_score(csv_path)


if __name__ == "__main__":
    mcp.run()