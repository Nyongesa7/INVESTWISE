def fetch_mmf_rates():
    import pandas as pd
    return pd.DataFrame({
        'Fund': ['CIC MMF', 'NCBA MMF', 'Madison MMF'],
        '7-Day Yield (%)': [10.21, 10.04, 9.87],
        'Risk': ['Low', 'Low', 'Low']
    })
