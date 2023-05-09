from django.shortcuts import render
import requests

def index(request):
    return render(request, 'index.html')

def get_bitcoin_price(request):
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = response.json()
    disclaimer = data['disclaimer']
    bitcoin_price_usd = data['bpi']['USD']['rate']
    bitcoin_price_gbp = data['bpi']['GBP']['rate']
    bitcoin_price_eur = data['bpi']['EUR']['rate']
    context = {
        'bitcoin_price_usd': bitcoin_price_usd,
        'bitcoin_price_gbp': bitcoin_price_gbp,
        'bitcoin_price_eur': bitcoin_price_eur,
        'disclaimer':disclaimer,
    }
    return render(request, 'bitcoin_price.html', context)
