.. _installation:

Installation
============

.. note:: upgrading from 0.8.7? Checkout :ref:`upgrading`.


Getting the latest release
--------------------------
lorem saldf	::

    $ pip install django-filer

If you are feeling adventurous you can get

Dependencies
------------

``django.contrib.staticfiles`` is required.


Configuration
-------------

Add ``"filer"`` and related apps to your project's ``INSTALLED_APPS`` setting and run ``manage.py syncdb``.::

    INSTALLED_APPS = [
        ...
        'filer',
        'easy_thumbnails',
        ...
    ]