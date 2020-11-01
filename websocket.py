import alpaca_trade_api as tradeapi
import threading
import time


# authentication and connection details
api_key = 'Insert_your_api_key_here'
api_secret = 'Insert_your_api_secret_here'
base_url = 'https://paper-api.alpaca.markets'


# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')


# init WebSocket
conn = tradeapi.stream2.StreamConn(
    api_key, api_secret, base_url=base_url, data_url=ws_url, data_stream='alpacadatav1'
)


@conn.on(r'^trade_updates$')
async def on_account_updates(conn, channel, account):
    print('account', account)


@conn.on(r'^status$')
async def on_status(conn, channel, data):
    print('status update', data)


@conn.on(r'^T.AAPL$')
async def trade_info(conn, channel, bar):
    print('bars', bar)
    print(bar._raw)


@conn.on(r'^Q.AAPL$')
async def quote_info(conn, channel, bar):
    print('bars', bar)


@conn.on(r'^AM.AAPL$')
async def on_minute_bars(conn, channel, bar):
    print('bars', bar)


# start websocket
def ws_start():
    conn.run(['account_updates', 'trade_updates', 'AM.AAPL', 'Q.AAPL', 'T.AAPL'])


ws_thread = threading.Thread(target=ws_start, daemon=True)
ws_thread.start()


# Let the websocket run for 30 seconds
time.sleep(30)
