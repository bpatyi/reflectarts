from django.contrib import admin
from exhibitions.models import Exhibition
from pictures.models import Picture
from django.conf import settings


class PictureInline(admin.TabularInline):
    model = Picture

class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'exhibitor', 'place', 'from_date', 'to_date', 'created_at', 'updated_at')
    inlines = [
        PictureInline,
    ]

    class Media:
        js = (settings.STATIC_URL + 'js/tiny_mce/tiny_mce.js',
            settings.STATIC_URL + 'js/textareas.js',)

admin.site.register(Exhibition, ExhibitionAdmin)
