from django.db import models

# Create your models here.
class Watchlist(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)

class Watching(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)

class Watched(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)

