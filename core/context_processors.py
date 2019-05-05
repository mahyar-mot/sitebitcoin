from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
#from django.http import JsonResponse
from ticket.models import Ticket


def crypto(request):
    session = Session()
    prices = []
    changes = []
    currencies = ['btc-usd','eth-usd','xrp-usd','ltc-usd',]
    url = 'https://api.cryptonator.com/api/ticker/'
    notification = Ticket.objects.all().filter(close=False).__len__()
    for i in currencies:
        try:
            response = session.get(url+i)
            data = json.loads(response.text)
            prices.append( "%.2f" % float(data['ticker']['price']))
            changes.append( "%.2f" % float(data['ticker']['change']))
        except (ConnectionError, Timeout, TooManyRedirects, ValueError) as e:
            print(e)
            prices.append(0)
            changes.append(0)
    data = {'bitcoinPrice':prices[0], 'ethriumPrice':prices[1], 'ripplePrice':prices[2], 'litePrice':prices[3],
            'bitcoinChange':changes[0], 'ethriumChange':changes[1], 'rippleChange':changes[2],'liteChange':changes[3],'notification':notification}
#    if request is not None:
#        return JsonResponse(data)
    return ( data )