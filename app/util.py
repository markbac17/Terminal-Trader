import hashlib
import requests
from .credentials import key

credentials = 'pk_09b201d4248943258cc92030525df8ae&'
symbol = 'aapl'

SALT = "random salt here".encode()

def hash_password(password):
    hashed_pw = hashlib.sha512(password.encode() + SALT).hexdigest()
    return hashed_pw

def get_price(ticker, credentials):
    #TODO: get price from IEX Cloud API
    response = requests.get('https://cloud.iexapis.com/stable/tops?token={}symbols={}'.format(credentials,ticker))
    data = response.json()
    return data[0]["lastSalePrice"]


print(get_price(symbol, credentials))

