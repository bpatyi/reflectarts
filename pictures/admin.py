from django.contrib import admin
from pictures.models import Picture

class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_exhibition_title', 'created_at', 'updated_at')

    def get_exhibition_title(self, obj):
        return '%s' % (obj.exhibition.title)

admin.site.register(Picture, PictureAdmin)
