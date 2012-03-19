
=========================
Django-keyboard-shortcuts
=========================

**Allow to use the keyboard instead of the mouse inside your web project**

The project code and bugtracker is hosted on
`Bitbucket <https://bitbucket.org/DNX/django-keyboard-shorcuts/>`_ and `Github <https://github.com/DNX/django-keyboard-shorcuts/>`_.

============
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


==============================
How to use keyboard_shortcuts?
==============================

If you have already installed keyboard_shortcus, you must proceed with the
configuration of your project.

Configuration
-------------
very simple, in three steps:

#. Add **keyboard_shortcuts** To INSTALLED_APPS

#. Modify Your settings.py, declare your **HOTKEYS** settings.

#. Add **{% load hotkeys %}{% setup_hotkeys %}** in your template.

Below the long explanation of each step...

Add keyboard_shortcuts To INSTALLED_APPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As with most Django applications, you should add **keyboard_shortcuts** to the INSTALLED_APPS within your settings file (usually *settings.py*).

Example::

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',

        # Added.
        'keyboard_shortcuts',
    ]

Modify Your settings.py
^^^^^^^^^^^^^^^^^^^^^^^

Within your *settings.py*, you’ll need to add some settings in order to assign to desired keyboard shortcuts some actions and to personalize the **django-keyboard-shortcuts** behaviour for your project.

You can define:

- **HOTKEYS** - a list containing the desired keyboard combinations and some settings for each (*default:* **list()**)
- **SPECIAL_DISABLED** - a bool, to disable shortcuts in some "**special cases**", when an input, a textarea or a select is active (*default:* **True**)

Example::

    # START keyboard_shortcuts settings #
    HOTKEYS = [
                {'keys': 'g + h',  # go home
                'link': '/'},
            ]
    SPECIAL_DISABLED = True
    # END keyboard_shortcuts settings #

Another advanced examples for HOTKEYS list::

    HOTKEYS = [
                {'keys': 'ctrl+h',  # home
                'link': '/',
                },
                {'keys': 'alt+w',
                'link': '/workspace/',
                },
                {'keys': 'shift+a',
                'link': '/about/',
                },
                {'keys': '1+2+3',
                'link': '/secret-url/',
                },
            ]

Available keys for your combinations:

- BACKSPACE
- TAB
- ENTER
- SHIFT
- CTRL
- ALT
- PAUSE
- CAPSLOCK
- ESC
- PAGE UP
- PAGE DOWN
- END
- HOME
- LEFT ARROW
- UP ARROW
- RIGHT ARROW
- DOWN ARROW
- INSERT
- DELETE
- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- A
- B
- C
- D
- E
- F
- G
- H
- I
- J
- K
- L
- M
- N
- O
- P
- Q
- R
- S
- T
- U
- V
- W
- X
- Y
- Z
- 0 (NUMPAD)
- 1 (NUMPAD)
- 2 (NUMPAD)
- 3 (NUMPAD)
- 4 (NUMPAD)
- 5 (NUMPAD)
- 6 (NUMPAD)
- 7 (NUMPAD)
- 8 (NUMPAD)
- 9 (NUMPAD)
- \*
- \+
- \-
- .
- /
- F1
- F2
- F3
- F4
- F5
- F6
- F7
- F8
- F9
- F10
- F11
- F12
- NUMLOCK
- SCROLL
- =
- COMMA
- SLASH /
- BACKSLASH \\
- META

Setup Hotkeys In Your Template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now all you need to do is to add **{% load hotkeys %}** and **{% setup_hotkeys %}** in yout template, and *django-keyboard-shortcuts* will do the rest for you... add event listeners and attend for any keypress.

The easiest way to do that is to do that is to load hotkeys **{% load hotkeys %}** at the **top** of your "base" template and to setup **{% setup_hotkeys %}** the in your **<head>** section.

Example of "base.html" template::

    {% load hotkeys %}
    <html>
        <head>
            <title>My title</title>
            {% setup_hotkeys %}
        </head>
        <body>
            my content...
        </body>
    </html>

==============================
How to test keyboard_shortcus?
==============================

Very simple::

    $ ./manage.py test keyboard_shortcus

=======
Credits
=======
Special thanks to the authors of this resources:

http://www.w3.org/2002/09/tests/keys.html

http://www.quirksmode.org/js/keys.html#t00

http://unixpapa.com/js/key.html

http://www.openjs.com/scripts/events/keyboard_shortcuts/

https://github.com/jeresig/jquery.hotkeys/


=========
Changelog
=========

0.0.6
---

* you can now configure in your settings.py the behaviour in "special cases"
* updated the documentation
* improved tests

0.0.5
-----

* disabled hotkeys in selet and text type inputs

0.0.4
-----

* now you can add multiple key combinations
* improved tests
* updated the documentation

0.0.3
-----

* included "keyboard_shortcuts/templates \*" in MANIFEST.in
* documentation updated
* templatetags and utils are now tested

0.0.2
-----

* added hotkeys templatetag
* added an example project for testing purposes

0.0.1
-----

* initial structure