import requests

def convert_currency(amount, from_currency, to_currency):
    try:
        url = f"https://open.er-api.com/v6/latest/{from_currency}"
        response = requests.get(url).json()
        rate = response['rates'][to_currency]
        return amount * rate
    except Exception:
        return None
