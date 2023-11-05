import os
import urllib.parse
import hashlib
import hmac
import base64
import requests
import time
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

api_url = "https://api.binance.us"

# get binanceus signature
def get_binanceus_signature(data, secret):
    postdata = urllib.parse.urlencode(data)
    message = postdata.encode()
    byte_key = bytes(secret, 'UTF-8')
    mac = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
    return mac

# Attaches auth headers and returns results of a POST request
def binanceus_request(uri_path, data, api_key, api_sec):
    headers = {
        'X-MBX-APIKEY': api_key
    }
    signature = get_binanceus_signature(data, api_sec)
    params = {
        **data,
        "signature": signature,
    }
    req = requests.get(api_url + uri_path, params=params, headers=headers)
    return req.text

# Retrieve API key and secret key from environment variables
api_key = os.getenv('BINANCE_API_KEY')
api_sec = os.getenv('BINANCE_SECRET_KEY')

# Ensure API key and secret key are available
if not api_key or not api_sec:
    raise Exception("API key and/or secret key not found. Please set them in your .env file.")

uri_path = "/sapi/v1/system/status"
data = {
    "timestamp": int(round(time.time() * 1000)),
}

result = binanceus_request(uri_path, data, api_key, api_sec)
print("GET {}: {}".format(uri_path, result))
