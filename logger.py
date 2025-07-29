# logger.py
import pandas as pd
import os
from datetime import datetime
from cbk_scraper import fetch_cbk_tbills_and_alert
from stock_data import fetch_nse_stocks
from mmf_data import fetch_mmf_rates
from banks import fetch_bank_rates

def save_weekly_log():
    today = datetime.today().strftime("%Y-%m-%d")
    folder = "logs"
    os.makedirs(folder, exist_ok=True)

    # CBK
    cbk = fetch_cbk_tbills_and_alert()
    cbk.to_csv(f"{folder}/cbk_{today}.csv", index=False)

    # Stocks
    stocks = fetch_nse_stocks()
    stocks.to_csv(f"{folder}/stocks_{today}.csv", index=False)

    # MMF
    mmf = fetch_mmf_rates()
    mmf.to_csv(f"{folder}/mmf_{today}.csv", index=False)

    # Banks
    banks = fetch_bank_rates()
    banks.to_csv(f"{folder}/banks_{today}.csv", index=False)

    print(f"✅ Weekly log saved: {today}")


from logger import save_weekly_log
save_weekly_log()
