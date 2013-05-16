from django.contrib import admin
from artists.models import Artist

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('title', 'website_url', 'created_at', 'updated_at')

admin.site.register(Artist, ArtistAdmin)
