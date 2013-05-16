from django.db import models


class NewsLetter(models.Model):
    title = models.CharField(max_length=80, verbose_name=u'title')
    url = models.URLField(max_length=200, verbose_name=u'url')

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'created at')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'updated at')

    def __unicode__(self):
        return u'%s' % self.title
