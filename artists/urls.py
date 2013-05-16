from django.conf.urls.defaults import patterns, include, url
from .views import ArtistList, Artist

urlpatterns = patterns('',
    url(r'^artists/$', ArtistList.as_view(), name='artists'),
    url(r'^artists/(?P<name>\w+)$', Artist.as_view(), name='artist'),
)
