import pandas as pd
from sqlalchemy import create_engine

# Example: Efficiently fetching 10 years of history for 500 companies
# Best Practice: Use chunks for large datasets

DB_CONNECTION = "postgresql://user:pass@host/finance_db"

def fetch_financials_bulk():
    engine = create_engine(DB_CONNECTION)

    query = """
    SELECT ticker, filing_date, revenue, net_income, free_cash_flow
    FROM financial_statements
    WHERE filing_date >= '2020-01-01'
    ORDER BY ticker, filing_date
    """

    print("🚀 Starting bulk export...")

    # Process in chunks of 10,000 rows to save memory
    chunks = pd.read_sql(query, engine, chunksize=10000)

    all_data = []
    for i, chunk in enumerate(chunks):
        print(f"📦 Processing chunk {i+1}...")
        # (Optional: Add transformation logic here)
        all_data.append(chunk)

    final_df = pd.concat(all_data)
    final_df.to_parquet("bulk_financials.parquet")
    print(f"✅ Export complete: {len(final_df)} rows saved to parquet.")

if __name__ == "__main__":
    fetch_financials_bulk()
