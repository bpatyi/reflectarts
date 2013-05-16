from django.contrib import admin
from subpages.models import Subpage

class SubpageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

admin.site.register(Subpage, SubpageAdmin)
