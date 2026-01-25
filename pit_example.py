"""
It shows a how to use your Point-in-Time (PIT) architecture to solve the hardest problem in backtesting: Look-ahead Bias.
"""
import snowflake.connector
import pandas as pd

# 1. Establish connection to the Snowflake Share
ctx = snowflake.connector.connect(
    user='<USER>',
    password='<PASSWORD>',
    account='<ACCOUNT_LOCATOR>',
    database='SEC_DATA_SHARE',
    schema='FINANCIALS'
)

def get_financials_as_of(ticker, knowledge_date):
    """
    Retrieves the most accurate financial data known to the market 
    on a specific historical date.
    """
    query = f"""
    SELECT 
        symbol,
        standard_concept,
        period_end,
        numeric_value,
        valid_from,
        valid_to
    FROM product_standard_pit_financials
    WHERE symbol = '{ticker}'
      -- This is the PIT Magic: 
      -- The knowledge_date must fall within the validity window.
      AND '{knowledge_date}' >= valid_from 
      AND ('{knowledge_date}' < valid_to OR valid_to IS NULL)
    ORDER BY period_end DESC;
    """
    
    return pd.read_sql(query, ctx)

# --- SCENARIO ---
# On June 1st, 2024, a quant is running a simulation. 
# They need to know the 'Net Income' for all companies.
# Even if a company restated their numbers in 2025, the quant 
# wants the version known ON June 1st, 2024.

sim_date = '2024-06-01'
df_backtest = get_financials_as_of('AAPL', sim_date)

print(f"Market Snapshot for AAPL as of {sim_date}:")
print(df_backtest.head())
