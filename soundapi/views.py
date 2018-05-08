from django.shortcuts import render
import requests

# Create your views here.
def searchIndex(request):
    urln = 'http://api.musixmatch.com/ws/1.1/track.search?apikey=1aa694f8617083fab82d3396a035c831&q_artist=justin%20bieber&page_size=3&page=1&s_track_rating=desc'
    city='Las Vegas'

    req=requests.get(urln).json()

    city_weather = {
        'track_n' : req['message']['body']['track_list'][0]['track']['track_name'],
                       'album_name': req['message']['body']['track_list'][0]['track']['album_name'],
        'img': req['message']['body']['track_list'][0]['track']['album_coverart_100x100'],
                       'url': req['message']['body']['track_list'][0]['track']['track_share_url'],


    }


    context = {'city_weather':city_weather}
    a=render(request,'soundapi/searchapi.html',context)
    return a

