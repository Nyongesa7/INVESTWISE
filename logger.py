def save_weekly_log():
    import pandas as pd, os, datetime
    from fetch_data import get_market_data

    data = get_market_data()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    log_path = "weekly_logs.csv"
    data['Date'] = today

    if os.path.exists(log_path):
        data.to_csv(log_path, mode='a', header=False, index=False)
    else:
        data.to_csv(log_path, index=False)
