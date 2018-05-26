from django.conf.urls import url
from .import views
from .views import GenresAPIView, GenresRetrieveView, ChannelsAPIView, ChannelRView, ShowsAPIView, ShowRuView, AllShowsAPIView

urlpatterns = [
    url(r'^genres/$', GenresAPIView.as_view(), name='genres'),
    url(r'^genres/(?P<type_head>[a-zA-Z0-9-]+)/$', GenresRetrieveView.as_view(), name='genre'),
    url(r'^genres/(?P<type_head>[a-zA-Z0-9-]+)/allshows/$', AllShowsAPIView.as_view(), name='allshows'),
    url(r'^genres/(?P<type_head>[a-zA-Z0-9-]+)/channels/$', ChannelsAPIView.as_view(), name='channels'),
    url(r'^genres/(?P<type_head>[a-zA-Z0-9-]+)/channels/(?P<title>[a-zA-Z0-9-]+)/$', ChannelRView.as_view(), name='channel'),
    url(r'^genres/(?P<type_head>[a-zA-Z0-9-]+)/channels/(?P<title>[a-zA-Z0-9-]+)/shows/$', ShowsAPIView.as_view(), name='shows'),    
    url(r'^genres/(?P<type_head>[a-zA-Z0-9-]+)/channels/(?P<title>[a-zA-Z0-9-]+)/shows/(?P<show_name>[a-zA-Z0-9-]+)/$', ShowRuView.as_view(), name='show'),    
]
