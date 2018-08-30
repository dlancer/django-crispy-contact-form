"""Implements contact form Subject model"""

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from ..conf import settings
from ..models.department import Department


@python_2_unicode_compatible
class Subject(models.Model):
    title = models.CharField(max_length=settings.CONTACT_FORM_SUBJECT_MAX_LENGTH)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    if hasattr(settings, 'SITE_ID') and settings.CONTACT_FORM_USE_SITES:
        from django.contrib.sites.models import Site
        site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'contact_form'
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')
