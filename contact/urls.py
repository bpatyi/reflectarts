from django.conf.urls.defaults import patterns, include, url
from .views import Contact

urlpatterns = patterns('',
    url(r'^contact/$', Contact.as_view(), name='contact'),
)
