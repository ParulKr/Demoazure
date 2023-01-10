from django.db import models

class moviel(models.Model):
    MovieName = models.CharField(max_length=100)
    Budget = models.IntegerField()
    IMDBrating = models.IntegerField()
    Movieinfo=models.CharField(max_length=400)
    link = models.CharField(max_length=400)
    image = models.ImageField(upload_to='Movielist/images')
    def __str__(self):
        return self.MovieName
# Create your models here.
