from django.db import models
from django.urls import reverse#red pk 1
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Album(models.Model):
    user=models.ForeignKey( User,unique=False,on_delete=models.CASCADE,null=True)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    gener = models.CharField(max_length=500)
    album_logo = models.FileField()
    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})
    def __str__(self):
        return  self.album_title+'-'+self.artist
# Create your models here.
class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=500)
    song_title = models.CharField(max_length=500)
    audio_file = models.FileField(default='',upload_to=u'mp3/', max_length=200)
    video_file = models.FileField(default='',upload_to=u'video/', max_length=200)

    is_favvioret=models.BooleanField(default=False)
    def __str__(self):
        return self.song_title
        return self.file_type

class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    city=models.CharField(max_length=500)
    phone=models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=Userprofile.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile,sender=User)