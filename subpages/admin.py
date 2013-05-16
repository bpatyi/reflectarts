from django.contrib import admin
from subpages.models import Subpage

class SubpageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

    class Media:
        js = (settings.STATIC_URL + 'js/tiny_mce/tiny_mce.js',
            settings.STATIC_URL + 'js/textareas.js',)

admin.site.register(Subpage, SubpageAdmin)
