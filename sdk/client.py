import pandas as pd
from sqlalchemy import create_engine, text


class FinancialDataClient:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def get_financials(self, ticker, start_date, point_in_time=True):
        """
        Fetches standardized financial statements.

        :param point_in_time: If True, returns data strictly as known on filing_date
                              (prevents look-ahead bias).
        """
        query = text("""
            SELECT 
                filing_date, 
                period_end_date, 
                revenue, 
                operating_income, 
                net_income,
                eps_diluted
            FROM financial_statements
            WHERE ticker = :ticker 
              AND filing_date >= :start_date
            ORDER BY filing_date ASC
        """)

        return pd.read_sql(query, self.engine, params={"ticker": ticker, "start_date": start_date})

    def get_comparables(self, sector):
        """Returns valuation multiples for a specific sector."""
        query = text("""
            SELECT ticker, company_name, ev_to_sales, p_e_ratio
            FROM valuation_multiples
            WHERE sector = :sector
        """)
        return pd.read_sql(query, self.engine, params={"sector": sector})
