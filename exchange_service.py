import requests
from config import settings

def fetch_currency(currency: str):
    try:

        url = f"{settings.api_url}/{currency}-BRL"

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        key = f"{currency}BRL"

        if key not in data:
            return None

        return float(data[key]["bid"])

    except Exception:
        return None
