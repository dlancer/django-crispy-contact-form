Customizable contact form based on crispy-forms
===============================================

``django-crispy-contact-form`` is a contact form based on crispy-forms with captcha support for Django 1.7+

.. image:: https://travis-ci.org/dlancer/django-crispy-contact-form.svg?branch=master
    :target: https://travis-ci.org/dlancer/django-crispy-contact-form/
    :alt: Build status

.. image:: https://img.shields.io/pypi/v/django-crispy-contact-form.svg
    :target: https://pypi.python.org/pypi/django-crispy-contact-form/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/django-crispy-contact-form.svg
    :target: https://pypi.python.org/pypi/django-crispy-contact-form/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/pypi/format/django-crispy-contact-form.svg
    :target: https://pypi.python.org/pypi/django-crispy-contact-form/
    :alt: Download format

.. image:: https://img.shields.io/pypi/l/django-crispy-contact-form.svg
    :target: https://pypi.python.org/pypi/django-crispy-contact-form/
    :alt: License


Requirements
------------

::

    Django>=1.7,<1.11
    Pillow>=3.4.2
    django-appcore>=0.0.9
    django-simple-captcha>=0.5.3
    django-crispy-forms>=1.6.1
    django-ipware>=1.1.6
    bleach>=1.5.0


Usage
=====

This contact form do not send messages or emails. All submitted information stored in the database
and optional Django signals generated about submission. You may setup your own handlers for these signals.

You can find detailed documentation in the "docs" directory.
