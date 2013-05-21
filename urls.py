from django.conf.urls.defaults import patterns, include, url
from django.contrib.flatpages.views import flatpage
from filebrowser.sites import site
from django.conf import settings

from core.views import Services

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reflect.views.home', name='home'),
    # url(r'^reflect/', include('reflect.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^services/', Services.as_view(), name='services'),

    url(r'^', include('core.urls')),
    url(r'^', include('contact.urls')),
    url(r'^', include('artists.urls')),
    url(r'^', include('exhibitions.urls')),
    url(r'^', include('newsletter.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.STATIC_URL.strip('/'), "django.views.static.serve", {"document_root": settings.STATIC_ROOT}),
    )
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}),
    )
