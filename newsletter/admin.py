from django.contrib import admin
from newsletter.models import NewsLetter

class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'date','created_at', 'updated_at')

admin.site.register(NewsLetter, NewsLetterAdmin)
