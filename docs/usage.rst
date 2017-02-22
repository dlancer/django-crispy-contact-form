Usage
=====

Start the development server and visit http://127.0.0.1:8000/admin/ to setup contact
form settings (you'll need the Admin app enabled).

Visit http://127.0.0.1:8000/contact_form/ to use contact form.

This contact form do not send messages or emails. All submitted information stored in the database
and optional Django signals generated after submission. You may setup your own handlers for these signals.

Configuration
=============

You must add these apps to your list of ``INSTALLED_APPS`` in ``settings.py``::

    INSTALLED_APPS = (
        ...
        'captcha',
        'crispy_forms',
        'contact_form',
    )

Include the contact form URLconf in your project urls.py like this::

    urlpatterns = patterns(
    '',
        ...
        url(r'^captcha/', include('captcha.urls')),
        url(r'^contact_form/', include('contact_form.urls')),
    )

Run ``python manage.py syncdb``.
This creates the appropriate tables in your database that are necessary for operation.

Database migration
------------------

Django 1.7+ has native database migration support.


Multilingual support
--------------------

All messages and text strings translatable with standard Django i18n framework.
Multilingual subjects supported with django-modeltranslation application. Default language is English.
If you want add more languages you should use sync_translation_fields command.
You may find more information in `django-modeltranslation documentation`_.

.. _`django-modeltranslation documentation`: https://django-modeltranslation.readthedocs.org/en/latest/


Customizing contact form
------------------------

You have a lot of options available to you to customize ``django-crispy-contact-form``.
These options should be defined in your ``settings.py`` file.

**Contact form customization**

* ``CONTACT_FORM_USE_CAPTCHA``: force use captcha for anonymous users

* ``CONTACT_FORM_USE_RECAPTCHA``: force use recaptcha for anonymous users

* ``CONTACT_FORM_USE_SIGNALS``: send signals after form submitting

* ``CONTACT_FORM_SUCCESS_URL``: url for redirection after successful form submission

* ``CONTACT_FORM_USE_SITES``: use Django Sites framework

* ``CONTACT_FORM_FILTER_SENDER_NAME``: filter sender name field

* ``CONTACT_FORM_FILTER_MESSAGE``: filter message field

* ``CONTACT_FORM_ALLOWED_MESSAGE_TAGS``: allowed html tags for message field

* ``CONTACT_FORM_STRIP_MESSAGE``: strip not allowed tags from message

**Contact form submission message customization**

* ``CONTACT_FORM_VALID_MESSAGE``: success message for valid form submission

* ``CONTACT_FORM_INVALID_MESSAGE``: error message for invalid form submission

**User model related customization**

* ``CONTACT_FORM_USE_USERNAME``: fill username form field for authenticated user

* ``CONTACT_FORM_USERNAME_FIELD``: username field name in User model

* ``CONTACT_FORM_USE_USER_EMAIL``: fill email form field for authenticated user

* ``CONTACT_FORM_USER_EMAIL_FIELD``: email field name in User model

**Contact form models fields customization**

* ``CONTACT_FORM_SENDER_NAME_MAX_LENGTH``: sender name maximum length

* ``CONTACT_FORM_SUBJECT_MAX_LENGTH``: message subject maximum length

* ``CONTACT_FORM_MESSAGE_MAX_LENGTH``: message text maximum length

* ``CONTACT_FORM_MESSAGE_MIN_LENGTH``: message text minimum length

* ``CONTACT_FORM_DEPARTMENT_NAME_MAX_LENGTH``: department name maximum length

* ``CONTACT_FORM_DEPARTMENT_PHONE_MAX_LENGTH``: department phone maximum length

* ``CONTACT_FORM_SUBJECTS_ORDER_BY``: field for subjects sorting (default: 'order')

**Contact form class and template customization**

* ``CONTACT_FORM_FORM_MODULE``: form module for contact form

   default: contact_form.forms.uniform

* ``CONTACT_FORM_FORM_CAPTCHA_MODULE``: form module for contact form with captcha

   default: contact_form.forms.uniform

Contact form modules included in ``django-crispy-contact-form`` package:

    contact_form.forms.bootstrap
    contact_form.forms.bootstrap3

You can create your own form modules with proper ContactForm and ContactFormCaptcha classes.

* ``CONTACT_FORM_FORM_TEMPLATE``: contact form template

    default: contact_form/form.html

**Contact form standard layout customization**

* ``CONTACT_FORM_RENDER_CANCEL_BUTTON``: render cancel button (default: False)

You can use your own javascript handler for cancel button if you enable this option.


Captcha rendering
-----------------

If you use ``django-simple-captcha`` package for rendering contact form with captcha support you
can override captcha field templates (see ``django-simple-captcha`` package documentation) for
proper form rendering. You can find recommended templates for ``uni_from`` template pack in the
``docs/example/templates/captcha`` folder within ``django-crispy-contact-form`` package documentation.

ReCaptcha support
-----------------

If you want use ReCaptcha service instead of ``django-simple-captcha`` application you should
install ``django-recaptcha`` application and use CONTACT_FORM_USE_RECAPTCHA option in your project settings.
Please notice what ``django-simple-captcha`` and ``django-recaptcha`` use the same package name for installation,
so if you need botch packages in your project, you should move one application to another directory.