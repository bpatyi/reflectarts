from django.contrib import admin
from pictures.models import Picture
from django.conf import settings

class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail', 'get_exhibition_title', 'created_at', 'updated_at')

    def get_exhibition_title(self, obj):
        return '%s' % (obj.exhibition.title)

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

admin.site.register(Picture, PictureAdmin)
