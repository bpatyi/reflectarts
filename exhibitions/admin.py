from django.contrib import admin
from exhibitions.models import Exhibition

class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'exhibitor', 'place', 'from_date', 'to_date', 'created_at', 'updated_at')

admin.site.register(Exhibition, ExhibitionAdmin)
