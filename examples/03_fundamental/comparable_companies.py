import pandas as pd
import matplotlib.pyplot as plt

# Example: Auto-generating a Comps Table for a specific sector

def generate_comps_table(df, sector="Technology"):
    # Filter by sector
    peers = df[df['sector'] == sector].copy()

    # Calculate Multiples
    peers['ev_to_sales'] = peers['enterprise_value'] / peers['revenue']
    peers['ev_to_ebitda'] = peers['enterprise_value'] / peers['ebitda']
    peers['p_e_ratio'] = peers['market_cap'] / peers['net_income']

    # Select key columns for the report
    report = peers[[
        'ticker', 'company_name', 'market_cap',
        'ev_to_sales', 'ev_to_ebitda', 'p_e_ratio'
    ]].set_index('ticker')

    # Clean up outliers for better viewing
    report = report[report['ev_to_sales'] < 20]

    return report.round(2)

# print(generate_comps_table(data, "SaaS"))
