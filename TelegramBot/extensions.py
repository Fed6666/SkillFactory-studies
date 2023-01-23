import requests
import json
from config import keys


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(from_currency: str, to_currency: str, amount: str):
        if to_currency == from_currency:
            raise APIException(f'Невозможно перевести одинаковые валюты {from_currency}.')
        try:
            to_currency_ticker = keys[to_currency]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {to_currency}")

        try:
            from_currency_ticker = keys[from_currency]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {from_currency}")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество валюты {amount}')

        if amount<= 0:
            raise APIException(f'Невозможно конверстировать количество валюты меньше или равное 0')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={from_currency_ticker}&tsyms={to_currency_ticker}')

        exchange_course = json.loads(r.content)[keys[to_currency]]
        total_amount = float(amount) * float(exchange_course)
        return total_amount