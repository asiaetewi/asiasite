from django.contrib import admin


# Register your models here.
from .models import Album
from .models import Song
from .models import Userprofile

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Userprofile)
