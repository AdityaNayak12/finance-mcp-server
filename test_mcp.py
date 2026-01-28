import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command="python3",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # --- KPI ---
            kpis = await session.call_tool(
                "compute_financial_kpis",
                arguments={"csv_path": "data/sample_data.csv"}
            )
            print("\n--- KPIs ---")
            print(kpis)

            # --- FORECAST ---
            forecast = await session.call_tool(
                "forecast",
                arguments={
                    "csv_path": "data/sample_data.csv",
                    "months": 6
                }
            )
            print("\n--- FORECAST ---")
            print(forecast)

            # --- VC SCORE ---
            vc = await session.call_tool(
                "investment_readiness",
                arguments={"csv_path": "data/sample_data.csv"}
            )
            print("\n--- VC SCORE ---")
            print(vc)


if __name__ == "__main__":
    asyncio.run(main())