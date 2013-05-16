from django.db import models
from autoslug import AutoSlugField


class Artist(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'title',)
    description = models.TextField(verbose_name=u'description',)
    slug = AutoSlugField(populate_from='title', slugify=lambda value: value.replace(' ','-'))

    image = ThumbnailerImageField(upload_to='artists', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'crated at')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'updated at')

    def __unicode__(self):
        return u'%s' % self.title
