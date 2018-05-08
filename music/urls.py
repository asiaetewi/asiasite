from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import password_reset_done,login,logout,password_reset
app_name='music'
urlpatterns = [

    url(r'^$',views.IndexView.as_view(),name="index" ),
    url(r'^register/$', views.register, name='register'),
    url(r'^search/$', views.searchIndex, name='search'),
    url(r'^weather/$', views.weatherIndex, name='weather'),
    url(r'^profile/$', views.view_profile, name='profile'),

    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),

    # music/<album_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    #music/album/2
    url(r'album/(?P<pk>[0-9]+)/$', views.UpdateAlbum.as_view(), name="album-update"),
#music/album/add
    url(r'album/add/$', views.CreateAlbum.as_view(), name="album-add"),
#music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.DeleteAlbum.as_view(), name="album-delete"),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.CreateAlbum.as_view(), name='create_song'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.CreateSong.as_view(), name='songs'),
    #music/myalbum
    url(r'^MyAlbum/$', views.AlbumView.as_view(), name='album'),

]

    # music/<album_id>/favoriet
