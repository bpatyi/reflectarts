from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'crated at')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'updated at')

    def __unicode__(self):
        return self.name
