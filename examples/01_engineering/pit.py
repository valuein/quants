from sdk.client import FinancialDataClient

# Connect using your issued credentials
client = FinancialDataClient(connection_string="postgresql://user:pass@host/finance_db")

# Get point-in-time financials for Apple (prevents look-ahead bias)
df = client.get_financials(ticker="AAPL", start_date="2020-01-01", point_in_time=True)
print(df.head())
