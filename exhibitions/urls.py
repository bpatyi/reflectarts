from django.conf.urls.defaults import patterns, include, url
from exhibitions.views import ExhibitionList, ExhibitionDetail

urlpatterns = patterns('',
    url(r'^exhibitions/$', ExhibitionList.as_view(), name='exhibitions'),
    url(r'^exhibitions/(?P<slug>\w+)$', ExhibitionDetail.as_view(), name='exhibition'),
)
