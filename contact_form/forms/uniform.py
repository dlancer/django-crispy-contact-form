"""Implements contact form forms for uni_form template pack"""

from __future__ import unicode_literals

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

from crispy_forms.layout import Layout, Fieldset, Button, ButtonHolder, Submit

from . import BaseContactForm
from ..conf import settings
from ..models import Message

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


class ContactForm(BaseContactForm):
    """ContactForm form"""

    def __init__(self, *args, **kwargs):
        """Form initialization method

        :param args: form args
        :param kwargs: form keyword args
        """
        self.helper = FormHelper()
        layout = Layout(
            Fieldset(
                _('Contact form'),
                'subject',
                'sender_name',
                'sender_email',
                'message',
            ),
            ButtonHolder(
                Button('cancel', _('Cancel'), css_class='secondaryAction'),
                Submit('submit', _('Submit'), css_class='primaryAction'),
            )
        )
        if not settings.CONTACT_FORM_RENDER_CANCEL_BUTTON:
            layout[1].pop(0)

        self.helper.add_layout(layout)
        self.helper.form_id = 'contact_form'
        self.helper.form_action = ''
        self.helper.form_method = 'POST'
        self.helper.form_style = 'inline'

        super(ContactForm, self).__init__(*args, **kwargs)

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
            layout = Layout(
                Fieldset(
                    _('Contact form'),
                    'subject',
                    'sender_name',
                    'sender_email',
                    'message',
                    'captcha',
                ),
                ButtonHolder(
                    Button('cancel', _('Cancel'), css_class='secondaryAction'),
                    Submit('submit', _('Submit'), css_class='primaryAction'),
                )
            )
            if not settings.CONTACT_FORM_RENDER_CANCEL_BUTTON:
                layout[1].pop(0)

            self.helper.add_layout(layout)
            self.helper.form_id = 'contact_form'
            self.helper.form_action = ''
            self.helper.form_method = 'POST'
            self.helper.form_style = 'inline'

            super(ContactForm, self).__init__(*args, **kwargs)
