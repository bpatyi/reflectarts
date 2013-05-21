from django.conf.urls.defaults import patterns, include, url
from newsletter.views import NewsLetterList

urlpatterns = patterns('',
    url(r'^newsletters/$', NewsLetterList.as_view(), name='newsletters'),
)
