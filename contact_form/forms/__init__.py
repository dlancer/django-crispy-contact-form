from __future__ import unicode_literals

import re

from django import forms
from django.utils.translation import ugettext_lazy as _

from ..conf import settings
from ..models import Subject

from django.core.exceptions import ImproperlyConfigured

try:
    import bleach
except ImportError:
    raise ImproperlyConfigured('django-crispy-contact-form application requires bleach package')


class BaseContactForm(forms.ModelForm):
    """ContactForm form"""

    if hasattr(settings, 'SITE_ID') and settings.CONTACT_FORM_USE_SITES:
        queryset = Subject.objects.filter(site__id=settings.SITE_ID).order_by(settings.CONTACT_FORM_SUBJECTS_ORDER_BY)
    else:
        queryset = Subject.objects.order_by(settings.CONTACT_FORM_SUBJECTS_ORDER_BY)
    subject = forms.ModelChoiceField(queryset=queryset,
                                     widget=forms.Select(),
                                     label=_('Message subject'),
                                     empty_label=_('Please select subject'),
                                     error_messages={'required': _('Please select subject')})
    sender_name = forms.CharField(label=_('Your name'),
                                  widget=forms.TextInput(
                                      attrs={'maxlength': settings.CONTACT_FORM_SENDER_NAME_MAX_LENGTH}
                                  ),
                                  error_messages={'required': _('Please enter your name')})
    # maxlength is 254 characters for compliant with RFCs 3696 and 5321
    sender_email = forms.EmailField(label=_('Your e-mail'),
                                    widget=forms.TextInput(attrs={'maxlength': 254}),
                                    error_messages={'required': _('Please enter your email')})
    message = forms.CharField(label=_('Your message'),
                              widget=forms.Textarea(attrs={'maxlength': settings.CONTACT_FORM_MESSAGE_MAX_LENGTH}),
                              min_length=settings.CONTACT_FORM_MESSAGE_MIN_LENGTH,
                              help_text=_('Your message ({0} characters minimum)').format(
                                  settings.CONTACT_FORM_MESSAGE_MIN_LENGTH
                              ),
                              error_messages={'required': _('Please enter your message'),
                                              'min_length': _('Use at least {0} characters').format(
                                                  settings.CONTACT_FORM_MESSAGE_MIN_LENGTH
                                              )})

    def clean_sender_name(self):
        data = self.cleaned_data['sender_name']
        if settings.CONTACT_FORM_FILTER_SENDER_NAME:
            if len(data) != len(bleach.clean(data, tags=[], strip=True)):
                raise forms.ValidationError(_('Not allowed characters in your name'))
        return data

    def clean_message(self):
        data = self.cleaned_data['message']
        if settings.CONTACT_FORM_LINKS_NOT_ALLOWED:
            m = re.search('(?P<url>https?://[^\s]+)', data)
            if m is not None:
                raise forms.ValidationError(_('Links not allowed'))
        return data
