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
diff = abs(t_minus_1_close - t_minus_2_close)
print(f"T-1 Close: {t_minus_1_close}, T-2 Close: {t_minus_2_close} / Diff: {diff} : 5% Diff: {t_minus_1_close * 0.05}")

# Has price changed by 5% or more
if diff >= t_minus_1_close * 0.05:

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
    print(f"Latest news on {STOCK}:")
    for line in headlines:
        print(f"\t{line}")

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

