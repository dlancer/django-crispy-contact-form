"""Implements contact form forms for bootstrap4 template pack"""

from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ImproperlyConfigured

try:
    import bleach
except ImportError:
    raise ImproperlyConfigured('django-crispy-contact-form application requires bleach package')

try:
    from crispy_forms.helper import FormHelper
except ImportError:
    raise ImproperlyConfigured('django-crispy-contact-form application requires django-crispy-forms package')

from crispy_forms.layout import Layout, Fieldset, Button, Submit
from crispy_forms.bootstrap import FormActions

from ..conf import settings
from ..models import Message, Subject

if settings.CONTACT_FORM_USE_RECAPTCHA:
    try:
        from captcha.fields import ReCaptchaField as CaptchaField
    except ImportError:
        raise ImproperlyConfigured('django-crispy-contact-form application requires django-recaptcha package')
elif settings.CONTACT_FORM_USE_CAPTCHA:
    try:
        from captcha.fields import CaptchaField
    except ImportError:
        raise ImproperlyConfigured('django-crispy-contact-form application requires django-simple-captcha package')


class ContactForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        """Form initialization method

        :param args: form args
        :param kwargs: form keyword args
        """
        self.helper = FormHelper()
        self.helper.label_class = settings.CONTACT_FORM_FORM_LABEL_CLASS
        self.helper.field_class = settings.CONTACT_FORM_FORM_FIELD_CLASS
        layout = Layout(
            Fieldset(
                _('Contact form'),
                'subject',
                'sender_name',
                'sender_email',
                'message',
            ),
            FormActions(
                Button('cancel', _('Cancel')),
                Submit('submit', _('Submit')),
            )
        )
        if not settings.CONTACT_FORM_RENDER_CANCEL_BUTTON:
            layout[1].pop(0)

        self.helper.add_layout(layout)
        self.helper.form_id = 'contact_form'
        self.helper.form_action = ''
        self.helper.form_method = 'POST'

        super(ContactForm, self).__init__(*args, **kwargs)

    def clean_sender_name(self):
        data = self.cleaned_data['sender_name']
        if settings.CONTACT_FORM_FILTER_SENDER_NAME:
            if len(data) != len(bleach.clean(data, tags=[], strip=True)):
                raise forms.ValidationError(_('Not allowed characters in your name'))
        return data

    class Meta:
        model = Message
        fields = (
            'subject',
            'sender_name',
            'sender_email',
            'message',
        )


if settings.CONTACT_FORM_USE_CAPTCHA or settings.CONTACT_FORM_USE_RECAPTCHA:
    class ContactFormCaptcha(ContactForm):
        """ContactForm form with captcha"""

        captcha = CaptchaField(label=_('Protection Code'),
                               error_messages={'required': _('Please enter protection code'),
                                               'invalid': _('Invalid protection code')})

        def __init__(self, *args, **kwargs):
            """Form initialization method

            :param args: form args
            :param kwargs: form keyword args
            """
            self.helper = FormHelper()
            self.helper.label_class = settings.CONTACT_FORM_FORM_LABEL_CLASS
            self.helper.field_class = settings.CONTACT_FORM_FORM_FIELD_CLASS
            layout = Layout(
                Fieldset(
                    _('Contact form'),
                    'subject',
                    'sender_name',
                    'sender_email',
                    'message',
                    'captcha',
                ),
                FormActions(
                    Button('cancel', _('Cancel')),
                    Submit('submit', _('Submit')),
                )
            )
            if not settings.CONTACT_FORM_RENDER_CANCEL_BUTTON:
                layout[1].pop(0)

            self.helper.add_layout(layout)
            self.helper.form_id = 'contact_form'
            self.helper.form_action = ''
            self.helper.form_method = 'POST'

            super(ContactForm, self).__init__(*args, **kwargs)
