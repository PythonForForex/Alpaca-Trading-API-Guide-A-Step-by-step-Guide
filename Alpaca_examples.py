import alpaca_trade_api as tradeapi
import threading

api_key = 'Insert_your_api_key_here'
api_secret = 'Insert_your_api_secret_here'
base_url = 'https://paper-api.alpaca.markets'

#instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

#obtain account information
account = api.get_account()
print(account)

'''init websocket - How do I use WebSockets to stream data with the Alpaca API? '''
conn = tradeapi.stream2.StreamConn(api_key, api_secret, base_url)

@conn.on(r'^account_updates$')
async def on_account_updates(conn, channel, account):
    print('account', account)

@conn.on(r'^trade_updates$')
async def on_trade_updates(conn, channel, trade):
    print('trade', trade)

def ws_start():
	conn.run(['account_updates', 'trade_updates'])

#start WebSocket in a thread
ws_thread = threading.Thread(target=ws_start, daemon=True)
ws_thread.start()

'''Data Examples - How do I get historical data from the Alpaca API?

aapl = api.polygon.historic_agg_v2('AAPL', 1, 'day', _from='2019-01-01', to='2019-02-01').df
aapl = api.get_barset('AAPL', 'day')
tsla = api.get_barset('TSLA', '15Min')
aapl = api.get_barset('AAPL', 'day', limit=1000)

'''


'''  How do I set a stop loss or take profit?
api.submit_order(symbol='TSLA', 
				qty=1, 
				side='buy', 
				time_in_force='gtc', 
				type='limit', 
				limit_price=400.00, 
				client_order_id=001, 
				order_class='bracket', 
				stop_loss=dict(stop_price='360.00'), 
				take_profit=dict(limit_price='440.00')
				)
'''

'''  Which stocks can you trade with Alpaca?
active_assets = api.list_assets(status='active')
for a in active_assets:
	print(a)
	print()
	print(type(a))


aapl_asset = api.get_asset('AAPL')
print(aapl_asset)
'''

#How do I find out what time the market closes?

print(api.get_clock())


'''  Get additional documentation for the REST API
help(tradeapi.REST)
'''