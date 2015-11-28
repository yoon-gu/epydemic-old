.. _installation:

Installation
============

.. warning:: No support ``python 3.x``.

Dependencies
------------

http://thenilblog.blogspot.kr/2015/01/install-pyqt-on-yosemite.html

#. Install Qt

	* run ``brew install qt``

#. Install SIP

	* run ``download SIP``
	* run ``python configure.py``
	* run ``make``
	* run ``sudo make install``

#. Install PyQt4

	* run ``download PyQt4``
	* run ``python configure.py``
	* run ``make``
	* run ``sudo make install``

#. Install pyqtgraph

	* run ``Download pyqtgraph``
	* run ``python setup.py install``

#. Install pyopengl

	* run ``sudo pip install pyopengl``


Configuration
-------------

Add ``"filer"`` and related apps to your project's ``INSTALLED_APPS`` setting and run ``manage.py syncdb``.::

    INSTALLED_APPS = [
        ...
        'filer',
        'easy_thumbnails',
        ...
    ]