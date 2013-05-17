from django.contrib import admin
from intros.models import Intro
from django.conf import settings

class IntroAdmin(admin.ModelAdmin):
    list_display = ('get_subpage_title', 'created_at', 'updated_at')

    def get_subpage_title(self, obj):
        return '%s' % (obj.subpage.name)

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )

admin.site.register(Intro, IntroAdmin)
