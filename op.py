import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

bun = float(btc['max_price']) - float(btc['min_price'])
siga = float(btc['opening_price'])
hi = float(btc['max_price'])

if (siga+bun) > hi:
    print("상승장")
else:
    print("하락장")