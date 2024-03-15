import json
import requests
from utils import config

HEADERS = {'APCA-API-KEY-ID': config.API_KEY, 'APCA-API-SECRET-KEY': config.API_SECRET}


def get_account():
    r = requests.get(config.ENDPOINT_URL, headers=HEADERS)
    return json.loads(r.content)


def place_order(symbol, qty, side, type, time_in_force):
    params = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }
    r = requests.post(config.ORDERS_URL, json=params, headers=HEADERS)
    return json.loads(r.content)


def get_orders():
    r = requests.get(config.ORDERS_URL, headers=HEADERS)
    return json.loads(r.content)


def get_bars(symbols, timeframe, start, limit):
    params = {
        'symbols': symbols,
        'timeframe': timeframe,
        'start': start,
        'limit': limit
    }
    r = requests.get(config.BARS_URL, params=params, headers=HEADERS)
    return json.loads(r.content)

