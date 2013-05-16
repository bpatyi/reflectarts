from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from autoslug import AutoSlugField

from exhibitions.models import Exhibition


class Picture(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'title', unique=True)
    description = models.TextField(verbose_name=u'description',)
    exhibition = models.ForeignKey(Exhibition, verbose_name=u'exhibition')
    slug = AutoSlugField(populate_from='title', slugify=lambda value: value.replace(' ','-'))

    image = ThumbnailerImageField(upload_to='pictures', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'crated at')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'updated at')

    def __unicode__(self):
        return u'%s' % self.title
