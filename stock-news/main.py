import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_Vantage_ApiKey = "key"
news_api_key = "key"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


account_sid = "key"
auth_token = "token"

alpha_vantage_parms = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": alpha_Vantage_ApiKey
}

r = requests.get(STOCK_ENDPOINT,params=alpha_vantage_parms)
r.raise_for_status()
data = r.json()["Time Series (Daily)"]
list_data = [value for (key,value) in data.items()]
yesterdays_data = list_data[0]

yesterdays_closing_price = yesterdays_data["4. close"]
print(yesterdays_closing_price)

Before_Yesterday_data = list_data[1]
before_yesterday_closing_price = Before_Yesterday_data["4. close"]
print(before_yesterday_closing_price)


possitive_diffrence = abs(float(yesterdays_closing_price) - float(before_yesterday_closing_price))
print(possitive_diffrence)
diffrence_percent = (possitive_diffrence / float(yesterdays_closing_price)) * 100
print(diffrence_percent)

if diffrence_percent > 5:
    print("get news")
    response = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2022-11-06&sortBy=publishedAt&apiKey=e6cd56e35cbf40bfb607f504efa6b12b")
    articles = response.json()["articles"]

    three_articles = articles[:3]





formatted_articles = [f"Headline: dfg{article['title']}\nBrief: {article['description']}" for article in three_articles]
print(formatted_articles)

client = Client(account_sid, auth_token)

for article in formatted_articles:
    message = client.messages.create(
                     body=article,
                     from_='twillo number',
                     to='your number'
                 )
