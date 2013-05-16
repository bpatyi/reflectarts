from django.contrib import admin
from intros.models import Intro

class IntroAdmin(admin.ModelAdmin):
    list_display = ('subpage__title', 'created_at', 'updated_at')

admin.site.register(Intro, IntroAdmin)
