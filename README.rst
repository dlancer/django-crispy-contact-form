Customizable contact form based on crispy-forms
===============================================

``django-crispy-contact-form`` is a contact form based on crispy-forms with captcha support for Django 1.5+

.. image:: https://travis-ci.org/dlancer/django-crispy-contact-form.svg?branch=master
    :target: https://travis-ci.org/dlancer/django-crispy-contact-form/
    :alt: Build status

.. image:: https://pypip.in/version/django-crispy-contact-form/badge.svg
    :target: https://pypi.python.org/pypi/django-crispy-contact-form/
    :alt: Latest PyPI version

.. image:: https://pypip.in/download/django-crispy-contact-form/badge.svg
    :target: https://pypi.python.org/pypi/django-crispy-contact-form/
    :alt: Number of PyPI downloads

.. image:: https://pypip.in/format/django-crispy-contact-form/badge.svg
    :target: https://pypi.python.org/pypi/django-crispy-contact-form/
    :alt: Download format

.. image:: https://pypip.in/license/django-crispy-contact-form/badge.svg
    :target: https://pypi.python.org/pypi/django-crispy-contact-form/
    :alt: License


Requirements
------------

::

    Django>=1.5
    django-appcore==0.0.3
    django-simple-captcha>=0.4.3
    django-crispy-forms>=1.4.0
    django-ipware>=0.0.8
    bleach>=1.4


Usage
=====

This contact form do not send messages or emails. All submitted information stored in the database
and optional Django signals generated about submission. You may setup your own handlers for these signals.

You may find detailed documentation is in the "docs" directory.
