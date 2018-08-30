Customizable contact form based on crispy-forms
===============================================

``django-crispy-contact-form`` is a contact form based on crispy-forms with captcha support for Django 1.11+

.. image:: https://travis-ci.org/dlancer/django-crispy-contact-form.svg?branch=master
    :target: https://travis-ci.org/dlancer/django-crispy-contact-form/
    :alt: Build status

.. image:: https://img.shields.io/pypi/v/django-crispy-contact-form.svg
    :target: https://pypi.python.org/pypi/django-crispy-contact-form/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/format/django-crispy-contact-form.svg
    :target: https://pypi.python.org/pypi/django-crispy-contact-form/
    :alt: Download format

.. image:: https://img.shields.io/pypi/l/django-crispy-contact-form.svg
    :target: https://pypi.python.org/pypi/django-crispy-contact-form/
    :alt: License


Requirements
------------

::

    Django>=1.11,<2.2
    django-appcore>=0.0.9
    django-crispy-forms==1.7.2
    django-ipware==2.1.0
    bleach==2.1.4



Optional Requirements
---------------------

::

    django-simple-captcha>=0.5.9
    django-recaptcha>=1.4.0

Usage
=====

This contact form do not send messages or emails. All submitted information stored in the database
and optional Django signals generated about submission. You may setup your own handlers for these signals.

You can find detailed documentation in the "docs" directory.
