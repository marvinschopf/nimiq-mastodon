import os
from dotenv import load_dotenv

load_dotenv()
import requests


def price(currency="USD"):
    return (
        requests.get(
            "https://api.nimiqx.com/price/"
            + currency
            + "?api_key="
            + os.getenv("NIMIQX_KEY")
        ).json()
    )[currency.lower()]
