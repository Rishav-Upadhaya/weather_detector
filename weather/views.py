from django.shortcuts import render
import json
import urllib.request
import os
# Create your views here.
API_KEY = os.getenv('OPEN_WEATHER_API_KEY')
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}+&appid={API_KEY}').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            # "coordinate": str(json_data['coord']['lon']) + ' ' +
            # str(json_data['coord']['lat']),
            "temp": int(json_data['main']['temp']-273.15),
            "feels_like": int(json_data['main']['feels_like']-273.15),
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "icon" : str(json_data['weather'][0]['icon']),
            "description" : str(json_data['weather'][0]['description']),
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})