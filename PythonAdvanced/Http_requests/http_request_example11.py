from django.shortcuts import render
import requests

#pipenv install django

def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'resources/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })

home(requests)