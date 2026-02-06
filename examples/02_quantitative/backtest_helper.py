from sdk.client import FinancialDataClient
import pandas as pd


# SCENARIO:
# We want to test a strategy that buys companies with growing Margins.
# CRITICAL: We must only use data available *before* the trade date to avoid cheating.

def get_valid_training_data(client, trade_date):
    print(f"📉 Fetching data universe known as of {trade_date}...")

    # Notice we filter by 'filing_date', NOT 'period_end_date'
    # This ensures we don't use Q4 earnings that weren't released yet.
    query = f"""
    SELECT ticker, revenue, operating_income
    FROM financial_statements
    WHERE filing_date < '{trade_date}'
    AND filing_date > '{trade_date}'::date - INTERVAL '90 days'
    """

    df = pd.read_sql(query, client.engine)
    df['operating_margin'] = df['operating_income'] / df['revenue']
    return df

# Usage
DATABASE_URL: str = "https://user:pass@host/finance_db"
client = FinancialDataClient(DATABASE_URL)
data = get_valid_training_data(client, "2024-01-15")
