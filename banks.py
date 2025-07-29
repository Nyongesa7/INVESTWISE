def fetch_bank_rates():
    import pandas as pd
    return pd.DataFrame({
        'Bank': ['Equity', 'KCB', 'Absa', 'Co-op'],
        'Savings Rate (%)': [6.5, 6.0, 5.8, 5.7]
    })
