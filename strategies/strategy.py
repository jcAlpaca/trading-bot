from utils import alpaca_api


def strategy(symbol, label, qty=1, type="market", time_in_force="gtc"):
    if label == 1:
        alpaca_api.place_order(symbol, qty, "buy", type, time_in_force)
    else:
        alpaca_api.place_order(symbol, qty, "sell", type, time_in_force)
