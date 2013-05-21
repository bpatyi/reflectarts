from django.conf.urls.defaults import patterns, include, url
from .views import ContactView

urlpatterns = patterns('',
    url(r'^contact/$', ContactView.as_view(), name='contact'),
)
