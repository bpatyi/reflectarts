from django.contrib import admin
from intros.models import Intro

class IntroAdmin(admin.ModelAdmin):
    list_display = ('get_subpage_title', 'created_at', 'updated_at')

    def get_subpage_title(self, obj):
        return '%s' % (obj.subpage.title)

    class Media:
        js = (settings.STATIC_URL + 'js/tiny_mce/tiny_mce.js',
            settings.STATIC_URL + 'js/textareas.js',)

admin.site.register(Intro, IntroAdmin)
