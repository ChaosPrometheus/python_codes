import time
import requests
import json
import hmac
import hashlib

api_key = 'eebO4tSpYJ5S5QbsFQ9qqyn1zKa278pBYL2jH0YG1W86i63OVkaMFEIu13mm8o3X'
api_secret = 'pEV9aHafKmnZNiPybsthzjXjy16KthODnvItx2s33iVOT6sy1YggwolheETqQvgg'
base_url = 'https://api.binance.com'

endpoint = '/api/v3/account'

params = {
    'timestamp': int(time.time() * 1000),  
    'recvWindow': 5000,  
}

query_string = '&'.join([f'{key}={params[key]}' for key in params])
signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
params['signature'] = signature
url = f'{base_url}{endpoint}'
response = requests.get(url, params=params, headers={'X-MBX-APIKEY': api_key})

if response.status_code == 200:
    account_info = response.json()
    for balance in account_info['balances']:
        if float(balance['free']) > 0 or float(balance['locked']) > 0:
            print(f"Asset: {balance['asset']}, Free: {balance['free']}, Locked: {balance['locked']}")
else:
    print(f"Ошибка при получении баланса. Код состояния: {response.status_code}")
    print(f"Текст ответа: {response.text}")
