from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import Genre, Channel, Show
from .serializers import GenreSerializers, ChannelSerializers, ShowSerializers

# Create your views here.
class GenresAPIView(generics.ListAPIView):
    lookup_field = 'type_head'
    serializer_class = GenreSerializers
    
    def get_queryset(self):
        return Genre.objects.all()
    


class GenresRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'type_head'
    serializer_class = GenreSerializers

    def get_queryset(self):
        return Genre.objects.all()

    # def get_serializer_context(self, *args, **kwargs):
    #     return {"request": self.request}


class ChannelsAPIView(generics.ListAPIView):
    lookup_field = 'title'
    serializer_class = ChannelSerializers

    def get_queryset(self):
        return Channel.objects.filter(genres__type_head=self.kwargs['type_head'])

    # def get_serializer_context(self, *args, **kwargs):
    #     return {"request": self.request}

class ChannelRView(generics.RetrieveAPIView):
    lookup_field = 'title'
    serializer_class = ChannelSerializers

    def get_queryset(self):
        qs = Channel.objects.filter(genres__type_head=self.kwargs['type_head'])
        qs = qs.filter(title = self.kwargs['title'])
        return qs

class ShowsAPIView(generics.ListAPIView):
    lookup_field = 'show_name'
    serializer_class = ShowSerializers

    def get_queryset(self):
        qs = Show.objects.filter(channels__title=self.kwargs['title'])
        return qs

class ShowRuView(generics.RetrieveUpdateAPIView):
    lookup_field = 'show_name'
    serializer_class = ShowSerializers

    def get_queryset(self):
        return Show.objects.filter(channels__title=self.kwargs['title'])


class AllShowsAPIView(generics.ListAPIView):
    lookup_field = 'show_name'
    serializer_class = ShowSerializers

    def get_queryset(self):
        return Show.objects.filter(channels__genres__type_head=self.kwargs['type_head'])
     