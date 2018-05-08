from django.shortcuts import render
import requests

# Create your views here.
def weatherIndex(request):
    urln = 'http://api.openweathermap.org/data/2.5/weather?q=gaza&units=imperial&appid=2398c9d11bf92c38bac9f03d1054d924'

    r=requests.get(urln).json()

    city_weather = {
        'city': 'gaza',
       'temperature': r['main']['temp'],
       'description': r['weather'][0]['description'],
       'icon': r['weather'][0]['icon']
    }


    context = {'city_weather':city_weather}
    a=render(request,'apisection/weather.html',context)
    return a

