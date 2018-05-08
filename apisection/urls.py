from django.conf.urls import url,include
from . import views
app_name='api'
urlpatterns = [
    url(r'^$',views.weatherIndex,name="weather" ),
]