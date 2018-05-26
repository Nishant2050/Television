from rest_framework import serializers
from .models import Genre, Channel, Show

class GenreSerializers(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model  = Genre
        fields = ['type_head',] 
    


class ChannelSerializers(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField(read_only=True)
    genres = GenreSerializers()
    class Meta:
        model  = Channel
        fields = ['genres','title',]

        

class ShowSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Show
        fields = ['id','channels','show_name','synopsis',] 
