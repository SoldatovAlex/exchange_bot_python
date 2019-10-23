import requests

from exchange_rate_bot import settings


def get_cur_price_btc():
    cur = requests.get(settings.URL_COINDESK_API_CUR_PRICE).json()['bpi']['USD']['rate']
    cur = float(cur.replace(',', ''))
    return cur
