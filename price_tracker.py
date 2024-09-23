import requests

def get_crypto_prices(symbols):
    """Fetches the current prices of multiple cryptocurrencies from a public API."""

    # Join the symbols into a comma-separated string for the API request
    ids = ','.join(symbols)

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    prices = {}
    for symbol in symbols:
        if symbol in data:
            prices[symbol] = float(data[symbol]['usd'])
        else:
            prices[symbol] = None  # Handle invalid symbol

    return prices

# Example usage with a list of cryptocurrencies
crypto_list = ['bitcoin', 'ethereum', 'dogecoin', 'litecoin']
prices = get_crypto_prices(crypto_list)

for symbol, price in prices.items():
    if price:
        print(f"The current price of {symbol} is ${price}")
    else:
        print(f"Invalid cryptocurrency symbol: {symbol}")