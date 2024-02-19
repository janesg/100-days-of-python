import os
import requests
from dotenv import load_dotenv

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()

## STEP 1: Use https://www.alphavantage.co/query
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yesterday's closing stock price.

ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

response = requests.get(url=STOCK_ENDPOINT,
                        params={
                            "function": "TIME_SERIES_DAILY",
                            "symbol": STOCK,
                            "apikey": ALPHA_VANTAGE_API_KEY
                        })

response.raise_for_status()

stock_data = response.json()
data_dates = list(stock_data["Time Series (Daily)"].keys())
t_minus_1_data = stock_data["Time Series (Daily)"][data_dates[1]]
t_minus_2_data = stock_data["Time Series (Daily)"][data_dates[2]]
t_minus_1_close = float(t_minus_1_data["4. close"])
t_minus_2_close = float(t_minus_2_data["4. close"])
diff = t_minus_1_close - t_minus_2_close
five_pct_t_minus_1_close = t_minus_1_close * 0.05
print(f"T-1 Close: {t_minus_1_close}, T-2 Close: {t_minus_2_close} / Diff: {diff} : 5% Diff: {five_pct_t_minus_1_close}")

# Has price changed by 5% or more
if abs(diff) >= five_pct_t_minus_1_close:
    indicator = "🔺" if diff >= 0.0 else "🔻"

    NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    response = requests.get(url=NEWS_ENDPOINT,
                            params={
                                "q": f"+{STOCK}",
                                # "q": f"+'{COMPANY_NAME}'",
                                # "sortBy": "publishedAt",
                                "pageSize": 3,
                                "apikey": NEWS_API_KEY
                            })

    response.raise_for_status()

    news_data = response.json()
    headlines = [article["title"] for article in news_data["articles"]]
    print(f"Latest news on {indicator}{STOCK}:")
    for line in headlines:
        print(f"\t{line}")
