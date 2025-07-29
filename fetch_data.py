import pandas as pd

def get_market_data():
    data = {
        "Asset": ["Treasury Bill", "NSE Stocks", "Money Market Fund", "Bank Savings"],
        "Return (%)": [13.5, 9.2, 10.3, 6.0],
        "Risk Level": ["Low", "High", "Moderate", "Low"]
    }
    return pd.DataFrame(data)
