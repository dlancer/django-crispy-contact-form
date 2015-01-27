
from contact_form.signals import contact_form_valid, contact_form_invalid


def my_callback1(sender, **kwargs):
    if kwargs['event'] == 'CONTACT_FORM_VALID_MESSAGE':
        print('Form submitted!')

contact_form_valid.connect(my_callback1)


def my_callback2(sender, **kwargs):
    if kwargs['event'] == 'CONTACT_FORM_INVALID_MESSAGE':
        print('Form not submitted!')

contact_form_invalid.connect(my_callback2)
