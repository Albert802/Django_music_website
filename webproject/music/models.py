from django.db import models

# Create your models here.

class Album(models.Model):
    album_title = models.CharField(max_length=1000)
    album_logo = models.FileField(default='')
    song_title = models.CharField(max_length=1000)
    price = models.IntegerField(default='')

    def __str__(self):
        return self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title= models.CharField(max_length=100)
    audio_file = models.FileField(default='')

    def __str__(self):
        return self.song_title

