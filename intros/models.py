from django.db import models
from subpages.models import Subpage

class Intro(models.Model):
    subpage = models.ForeignKey(Subpage, unique=True)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'crated at')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'updated at')

    def __unicode__(self):
        return self.content
