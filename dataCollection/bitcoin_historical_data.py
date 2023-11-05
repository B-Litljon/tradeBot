# Function to fetch historical Bitcoin data
def get_bitcoin_historic_data(interval, start_str, end_str=None):
    endpoint = '/api/v1/klines'
    symbol = 'BTCUSDT'
    params = {
        'symbol': symbol,
        'interval': interval,
        'startTime': start_str,
        'endTime': end_str
    }
    response = requests.get(api_url + endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching historical data: {}".format(response.status_code))

# Define the interval and start date for the Bitcoin data
interval = '1h'     # 1-hour intervals
start_str = '1 Jan, 2020'  # Start date

# Fetch the historical Bitcoin data
historic_bitcoin_data = get_bitcoin_historic_data(interval, start_str)
