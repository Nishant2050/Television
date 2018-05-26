from django.db import models
from rest_framework.reverse import reverse

# Create your models here.
class Genre(models.Model):
    type_head = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.type_head

        

    
class Channel(models.Model):
    genres = models.ForeignKey(Genre, related_name='genre', on_delete=models.CASCADE) 
    title  = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title


class Show(models.Model):
    channels  = models.ForeignKey(Channel, related_name='chan', on_delete=models.CASCADE)
    show_name = models.CharField(max_length=30, unique=True)
    synopsis  = models.TextField(max_length=500, null=True, blank=True)
    show_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.show_name
