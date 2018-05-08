from django.conf.urls import url,include
from . import views
app_name='sound'
urlpatterns = [
    url(r'^$',views.searchIndex,name="search" ),
]