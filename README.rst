
===========================================================================
django-keyboard-shortcuts: DJANGO Background Image Slideshow + NAVIgation
===========================================================================

Django Keyboard Shortcuts
=========================

**Allow to use the keyboard instead of the mouse inside your web project**

What Is a Keyboard Shortcut?
----------------------------
From Wikipedia: Keyboard shortcuts are typically an alternate means for invoking one or more commands that would otherwise be accessible only through a menu, a pointing device, different levels of a user interface, or via a command console. Keyboard shortcuts generally expedite common operations by reducing input sequences to a few keystrokes, hence the term "shortcut".

Learn more here: http://en.wikipedia.org/wiki/Keyboard_shortcut

Installation
============

There are a few different ways to install keyboard_shortcus:

Using pip
---------
If you have pip install available on your system, just type::

    pip install django-keyboard-shortcuts

If you've already got an old version of keyboard_shortcus, and want to upgrade, use::

    pip install -U django-keyboard-shortcuts

Installing from a directory
---------------------------
If you've obtained a copy of keyboard_shortcus using either Mercurial or a downloadable
archive, you'll need to install the copy you have system-wide. Try running::

    python setup.py develop

If that fails, you don't have ``setuptools`` or an equivalent installed;
either install them, or run::

    python setup.py install


How to use keyboard_shortcus?
=============================

If you have already installed keyboard_shortcus, you must proceed with the
configuration of your project.

Configuration
-------------

First of all you must...

Key and Character Codes
-----------------------
Very helpful pages resources here:
http://www.w3.org/2002/09/tests/keys.html
http://www.quirksmode.org/js/keys.html#t00

How to test keyboard_shortcus?
==============================

**Please** test keyboard_shortcus before using it in your project:

$ ./manage.py test keyboard_shortcus