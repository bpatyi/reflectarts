from django.contrib import admin
from subpages.models import Subpage
from intros.models import Intro
from django.conf import settings


class IntroInline(admin.StackedInline):
    model = Intro


class SubpageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created_at', 'updated_at')
    inlines = [
        IntroInline,
    ]

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )

admin.site.register(Subpage, SubpageAdmin)
