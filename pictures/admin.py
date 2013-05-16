from django.contrib import admin
from pictures.models import Picture

class PictureAdmin(admin.ModelAdmin)
    list_display = ('title', 'exhibition__title', 'crated_at', 'updated_at')
