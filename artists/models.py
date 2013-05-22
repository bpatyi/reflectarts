from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from autoslug import AutoSlugField
from django.conf import settings


class Artist(models.Model):
    first_name = models.CharField(max_length=128, verbose_name=u'first name', help_text="First name of artist")
    last_name = models.CharField(max_length=128, verbose_name=u'last name', help_text="Last name of artist")
    email = models.EmailField(default=settings.REFLECT_NOTIFY_EMAIL)
    description = models.TextField(verbose_name=u'description', blank=True, null=True)
    slug = AutoSlugField(populate_from='get_name', slugify=lambda value: value.replace(' ','-'))
    website_url = models.URLField(null=True, blank=True,)

    selected = models.BooleanField(default=False, verbose_name="Represented", help_text="Whether to display on index page (represented)")

    image = ThumbnailerImageField(upload_to='artists', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'crated at')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'updated at')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_name(self):
        return u'%s %s' % (self.first_name, self.last_name)
