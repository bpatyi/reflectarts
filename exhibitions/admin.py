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
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )

admin.site.register(Exhibition, ExhibitionAdmin)
