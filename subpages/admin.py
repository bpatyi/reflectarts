from django.contrib import admin
from subpage.models import Subpage

class SubpageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

admin.site.register(Subpage, SubpageAdmin)
