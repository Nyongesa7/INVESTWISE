def get_market_data():
    import pandas as pd
    return pd.DataFrame({
        'Asset': ['Treasury Bills', 'NSE Stocks', 'Money Market Funds', 'Bank Savings'],
        'Return (%)': [13.8, 9.1, 10.4, 6.2],
        'Risk': ['Low', 'High', 'Moderate', 'Low']
    })
