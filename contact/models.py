from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default='')
    email = models.EmailField()
    description = models.TextField(blank=True, null=True, default='')
    phone = models.CharField(max_length=20, default='', blank=True, null=True,)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'crated at')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'updated at')

    def __unicode__(self):
        return self.name
