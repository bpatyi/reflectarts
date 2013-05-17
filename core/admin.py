from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminBase

class FlatPageAdmin(FlatPageAdminBase):
    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
