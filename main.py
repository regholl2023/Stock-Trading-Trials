import alpaca_trade_api as tradeapi
from tickers import sp500
import yfinance as yf 

API_KEY = "PK53MZ4MH9XBPI4H9NV0"
SECRET_KEY = "z1ifxefIvc6tV75bt8ZcAgwOyyJ7l4oAzAe6wB6L"
BASE_URL = "https://paper-api.alpaca.markets"  # Use paper trading URL

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

account_info = api.get_account()
print(account_info)
positions = api.list_positions()
print(positions)

ticker = "AAPL"  
stock_data = yf.Ticker(ticker)

hist = stock_data.history(period="5d")
print(hist)

real_time_data = stock_data.history(period="1d", interval="1m")
print(real_time_data)