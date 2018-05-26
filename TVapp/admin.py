from django.contrib import admin
from .models import Genre, Channel, Show

# Register your models here.
admin.site.register(Genre)
admin.site.register(Channel)
admin.site.register(Show)