from django.conf.urls.defaults import patterns, include, url
from .views import ArtistList, ArtistDetail

urlpatterns = patterns('',
    url(r'^artists/$', ArtistList.as_view(), name='artists'),
    url(r'^artists/(?P<slug>\w+)$', ArtistDetail.as_view(), name='artist'),
)
