import requests

def get_crypto_price(symbol):
    """Fetches the current price of a cryptocurrency from a public API."""

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    if symbol in data:
        return data[symbol]['usd']
    else:
        return None  # Handle invalid symbol

# Example usage
price = get_crypto_price('bitcoin')
if price:
    print(f"The current price of Bitcoin is ${price}")
else:
    print("Invalid cryptocurrency symbol")
