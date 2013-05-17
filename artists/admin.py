from django.contrib import admin
from artists.models import Artist
from django.conf import settings

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('title', 'website_url', 'created_at', 'updated_at')

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )

admin.site.register(Artist, ArtistAdmin)
