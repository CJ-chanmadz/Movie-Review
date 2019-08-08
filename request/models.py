from django.db import models
from django.urls import reverse

# Create your models here.
class Request(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=1000)
    email = models.CharField(max_length=50)
    movie_title = models.CharField(max_length=2083)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('request')