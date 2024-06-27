from django.db import models


# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    position = models.IntegerField(default=0)
