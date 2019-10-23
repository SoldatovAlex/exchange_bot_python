import json

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

from core.btc_api import get_cur_price_btc
from core.telegram_api import invoke_telegram


@csrf_exempt
def telegram_hook(request):
    update = json.loads(request.body)
    if 'message' not in update:
        return HttpResponse('OK')
    message = update['message']

    text = ''
    if 'text' in message:
        text = message['text']

    if '/start' in text:
        invoke_telegram('sendMessage', chat_id=update['message']['chat']['id'], text='Hello world')
    elif '/getprice' in text:
        current_price = get_cur_price_btc()
        invoke_telegram('sendMessage', chat_id=update['message']['chat']['id'], text=current_price)

    return HttpResponse('OK')
