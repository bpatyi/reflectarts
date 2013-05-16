from django.contrib import admin
from pictures.models import Picture
from django.conf import settings

class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_exhibition_title', 'created_at', 'updated_at')

    def get_exhibition_title(self, obj):
        return '%s' % (obj.exhibition.title)

    class Media:
        js = (settings.STATIC_URL + 'js/tiny_mce/tiny_mce.js',
            settings.STATIC_URL + 'js/textareas.js',)

admin.site.register(Picture, PictureAdmin)
