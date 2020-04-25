import alpaca_trade_api as tradeapi

#authentication and connection details
api_key = 'Insert_your_api_key_here'
api_secret = 'Insert_your_api_secret_here'
base_url = 'https://paper-api.alpaca.markets'

#instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

#obtain account information
account = api.get_account()
print(account)