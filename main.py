import matplotlib.pyplot as plt
from datetime import datetime

# Example bar data
bar_data = alpaca_api.get_bars('AAPL', "1T")
# Extracting data
timestamps = [datetime.fromisoformat(bar['t'][:-1]) for bar in bar_data['AAPL']]
opens = [bar['o'] for bar in bar_data['AAPL']]
highs = [bar['h'] for bar in bar_data['AAPL']]
lows = [bar['l'] for bar in bar_data['AAPL']]
closes = [bar['c'] for bar in bar_data['AAPL']]
volumes = [bar['v'] for bar in bar_data['AAPL']]

# Plotting candlestick chart
fig, ax = plt.subplots()
ax.plot(timestamps, opens, label='Open', color='blue', linestyle='-', linewidth=1)
ax.plot(timestamps, closes, label='Close', color='red', linestyle='-', linewidth=1)
ax.vlines(timestamps, lows, highs, color='black', linewidth=1)
ax.fill_between(timestamps, lows, highs, color='grey', alpha=0.3)
ax.set_xlabel('Timestamp')
ax.set_ylabel('Price')
ax.set_title('AAPL Candlestick Chart')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
