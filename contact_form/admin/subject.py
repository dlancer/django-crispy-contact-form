"""Implements contact form admin interface"""

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html

from django.urls import reverse

from django.utils.translation import ugettext as _

from contact_form.conf import settings
from contact_form.models import Subject


try:
    from modeltranslation.admin import TranslationAdmin

    class SubjectBaseAdmin(TranslationAdmin):
        pass
except ImportError:
    class SubjectBaseAdmin(admin.ModelAdmin):
        pass


class SubjectAdmin(SubjectBaseAdmin):
    if hasattr(settings, 'SITE_ID') and settings.CONTACT_FORM_USE_SITES:
        list_display = ('title', 'department_url', 'site', 'order',)
    else:
        list_display = ('title', 'department_url', 'order',)
        exclude = ('site',)
    list_editable = ('order',)
    ordering = ('order',)

    def department_url(self, obj):
        change_url = reverse('admin:contact_form_department_change', args=(obj.department.pk,))
        return format_html('<a href="{}">{}</a>', change_url, obj.department.name)

    department_url.allow_tags = True
    department_url.short_description = _('Department')


admin.site.register(Subject, SubjectAdmin)
