import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("API_KEY")


def convert_transaction(transaction: dict) -> Any:
    url = "https://api.apilayer.com/currency_data/convert"
    headers = {"apikey": apikey}
    payload = {
        "amount": transaction["operationAmount"]["amount"],
        "from": transaction["operationAmount"]["currency"]["code"],
        "to": "RUB",
    }
    response = requests.get(url, headers=headers, params=payload)
    result = response.json()
    return round(result["result"], 2)
