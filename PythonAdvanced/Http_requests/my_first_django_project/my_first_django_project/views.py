from django.shortcuts import render
import requests

# View for Django MVC example

def home(request):
    response = requests.get('https://freegeoip.live/json/')
    geodata = response.json()
    return render(request, 'home.html', { # html template - resources/home.html
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })

