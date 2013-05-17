from django.contrib import admin
from pictures.models import Picture
from django.conf import settings

class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_exhibition_title', 'created_at', 'updated_at')

    def get_exhibition_title(self, obj):
        return '%s' % (obj.exhibition.title)

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )

admin.site.register(Picture, PictureAdmin)
