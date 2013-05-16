from django.contrib import admin
from intros.models import Intro

class IntroAdmin(admin.ModelAdmin):
    list_display = ('get_subpage_title', 'created_at', 'updated_at')

    def get_subpage_title(self, obj):
        return '%s' % (obj.subpage.title)

admin.site.register(Intro, IntroAdmin)
