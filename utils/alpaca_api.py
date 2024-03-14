import requests
import config

ACCOUNT_URL = config.ACCOUNT_URL
r = requests.get(config.ENDPOINT_URL, headers={'APCA-API-KEY-ID': config.API_KEY, 'APCA-API-SECRET-KEY': config.API_SECRET})
print(r.content)
