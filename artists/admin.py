from django.contrib import admin
from artists.models import Artist
from django.conf import settings

from easy_thumbnails.files import get_thumbnailer


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'website_url', 'created_at', 'updated_at')

    def image_thumbnail(self, obj):
        thumb_url = get_thumbnailer(obj.image)['avatar'].url

        if obj.image and thumb_url:
            return '<img src="%s" />' % thumb_url
        else:
            return ""

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = "Thumbnail"

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )

admin.site.register(Artist, ArtistAdmin)
