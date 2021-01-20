from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class FirstSlide(models.Model):
    image = models.ImageField(_('Image'), upload_to='media/images')
    slug = models.CharField(_('Slug'), max_length=20)

    class Meta:
        verbose_name = _('FirstSlide')
        verbose_name_plural = _('FirstSlides')
