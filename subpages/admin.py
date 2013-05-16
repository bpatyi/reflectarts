from django.contrib import admin
from subpages.models import Subpage
from intros.models import Intro
from django.conf import settings


class IntroInline(admin.TabularInline):
    model = Intro


class SubpageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created_at', 'updated_at')
    inlines = [
        IntroInline,
    ]

    class Media:
        js = (settings.STATIC_URL + 'js/tiny_mce/tiny_mce.js',
            settings.STATIC_URL + 'js/textareas.js',)

admin.site.register(Subpage, SubpageAdmin)
