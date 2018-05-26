from rest_framework import serializers
from .models import Genre, Channel, Show

class GenreSerializers(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model  = Genre
        fields = ['type_head',] 
    
    # def get_url(self, obj):
    #     request = self.context.get("request")
    #     return obj.get_genre_url(request=request)



class ChannelSerializers(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField(read_only=True)
    genres = GenreSerializers()
    class Meta:
        model  = Channel
        fields = ['genres','title',]

    # def get_url(self, obj):
    #     request = self.context.get("request")
    #     return obj.get_channel_url(request=request)


class ShowSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Show
        fields = ['id','channels','show_name','synopsis',] 