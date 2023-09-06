import alpaca_trade_api as tradeapi
from tickers import sp500

API_KEY = "PK53MZ4MH9XBPI4H9NV0"
SECRET_KEY = "z1ifxefIvc6tV75bt8ZcAgwOyyJ7l4oAzAe6wB6L"
BASE_URL = "https://paper-api.alpaca.markets"  # Use paper trading URL

api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

account_info = api.get_account()
print(account_info)

positions = api.list_positions()

timeframe = '1D'  # 1 day candles
start_date = '2022-01-01'
end_date = '2022-08-31'

stock_data = {}
for symbol in sp500:
    stock_data[symbol] = api.get_asset(symbol, timeframe, start=start_date, end=end_date).df[symbol]
print(stock_data)