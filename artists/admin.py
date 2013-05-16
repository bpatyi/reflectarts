from django.contrib import admin
from artists.models import Artist
from django.conf import settings

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('title', 'website_url', 'created_at', 'updated_at')

    class Media:
        js = (settings.STATIC_URL + 'js/tiny_mce/tiny_mce.js',
            settings.STATIC_URL + 'js/textareas.js',)

admin.site.register(Artist, ArtistAdmin)
