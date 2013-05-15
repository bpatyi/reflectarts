from django.db import models

class Subpage(models.Model):
    name = models.CharField(max_length=80)
    content = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'crated at')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'updated at')

    def __unicode__(self):
        return self.name
