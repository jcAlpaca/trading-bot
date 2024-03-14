import json
import requests
from config import *

HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': API_SECRET}


def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)


def create_order(symbol, qty, side, type, time_in_force):
    params = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }
    r = requests.post(ORDERS_URL, json=params, headers=HEADERS)
    return json.loads(r.content)


def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(r.content)


def get_bars(symbols, timeframe):
    params = {
        'symbols': symbols,
        'timeframe': timeframe
    }
    r = requests.get(BARS_URL, params=params, headers=HEADERS)
    return json.loads(r.content)


import matplotlib.pyplot as plt
from datetime import datetime

# Example bar data
bar_data = get_bars('AAPL', "1T")['bars']['AAPL']
for bar in bar_data:
    print(bar)
