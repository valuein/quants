import pandas as pd
import numpy as np

# Example: calculating a 'Quality' factor using ROIC and Debt/EBITDA

def calculate_factors(df):
    # 1. Calculate ROIC (Return on Invested Capital)
    # NOPAT / Invested Capital
    df['nopat'] = df['operating_income'] * (1 - 0.21) # approx tax rate
    df['invested_capital'] = df['total_equity'] + df['total_debt'] - df['cash_equivalents']

    df['roic'] = df['nopat'] / df['invested_capital']

    # 2. Filtering for High Quality
    # Rules: ROIC > 15% and Revenue Growth > 10%
    high_quality = df[
        (df['roic'] > 0.15) &
        (df['revenue_growth_yoy'] > 0.10)
        ]

    return high_quality.sort_values(by='roic', ascending=False)

# Mock usage (assuming df is loaded)
# top_picks = calculate_factors(data)
# print(top_picks[['ticker', 'roic', 'revenue_growth_yoy']].head(10))
