from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm
from django.urls import reverse_lazy
from .models import Album,Song
import requests
from django.shortcuts import render_to_response



def view_profile(request):
    args={'user':request.user}
    return render(request,'music/profile.html',args)

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Album.objects.all()


class AlbumView(generic.ListView):
    template_name = 'music/album.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)

class SongView(generic.ListView):
    template_name = 'music/songs.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Song.objects.all()

class DetailView(generic.DetailView):
    model =Album
    template_name = 'music/detail.html'




class CreateAlbum(CreateView):
    model = Album

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateAlbum, self).form_valid(form)
    fields = ['artist','album_title','gener','album_logo']

class CreateSong(CreateView):
    model = Song
    fields = ['album','file_type','song_title','audio_file','video_file']

class UpdateAlbum(UpdateView):
    model = Album
    fields = ['artist','album_title','gener','album_logo']


class DeleteAlbum(DeleteView):
    model = Album
    success_url= reverse_lazy('music:index')



def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'music/registration_form.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)
def searchIndex(request):
    template='music/searchapi.html'
    query=request.POST.get('q')
    urln = 'http://api.musixmatch.com/ws/1.1/track.search?apikey=1aa694f8617083fab82d3396a035c831&q_artist={}&page_size=3&page=1&s_track_rating=desc'

    req=requests.get(urln.format(query)).json()

    track_info = {
        'track_n' : req['message']['body']['track_list'][0]['track']['track_name'],
                       'album_name': req['message']['body']['track_list'][0]['track']['album_name'],
        'img': req['message']['body']['track_list'][0]['track']['album_coverart_100x100'],
                       'url': req['message']['body']['track_list'][0]['track']['track_share_url'],


    }


    context = {'track_info':track_info}
    a=render(request,'music/searchapi.html',context)
    return a


def weatherIndex(request):
    urln = 'http://api.openweathermap.org/data/2.5/weather?q=gaza&units=imperial&appid=2398c9d11bf92c38bac9f03d1054d924'

    r=requests.get(urln).json()

    city_weather = {
        'city': 'gaza',
       'temperature': r['main']['temp'],
       'description': r['weather'][0]['description'],
        'clear': r['weather'][0]['main'],

        'icon': r['weather'][0]['icon']
    }


    context = {'city_weather':city_weather}
    a=render(request,'music/weather.html',context)
    return a


