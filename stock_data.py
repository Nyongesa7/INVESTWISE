def fetch_nse_stocks():
    import pandas as pd
    return pd.DataFrame({
        'Company': ['Safaricom', 'KCB', 'Equity', 'EABL'],
        'Price': [16.3, 39.5, 43.2, 165.5],
        '1W Change (%)': [1.2, -0.5, 2.1, 0.3]
    })
