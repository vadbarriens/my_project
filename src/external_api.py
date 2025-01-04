import requests
import os
from dotenv import load_dotenv


load_dotenv()
apikey = os.getenv('API_KEY')

def convert_transaction(transaction: dict) -> float:
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        url = "https://api.apilayer.com/currency_data/convert"
        headers = {
            "apikey": apikey
        }
        payload = {
            "amount": transaction['operationAmount']['amount'],
            "from": transaction['operationAmount']['currency']['code'],
            "to": "RUB"
        }
        response = requests.get(url, headers=headers, params=payload)
        result = response.json()
        return round(result['result'], 2)



if __name__ in '__main__':
    print(
        convert_transaction(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    )
    )
