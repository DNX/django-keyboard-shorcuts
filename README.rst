
=========================
Django-keyboard-shortcuts
=========================

**Helps to use the keyboard inside your web project**

The project code and bugtracker is hosted on
`Bitbucket <https://bitbucket.org/DNX/django-keyboard-shorcuts/>`_ and `Github <https://github.com/DNX/django-keyboard-shorcuts/>`_.

Don't uses any javascript framework!
------------------------------------

On the client side you will have only pure javascript code that receives all pre-elaborated and optimized data directly from django.

The only dependency is Django itself
------------------------------------
Just **install**, **configure**, and you are ready to **dominate the world** with your website keyboard shortcuts.

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

More about HOTKEYS setting?
"""""""""""""""""""""""""""

HOTKEYS is a list of dictioanaries. Each dictionary contains the attributes for a particular keyboard combination. HOTKEYS dist must have a key called "**keys**" and one of "**link**" or "**js**".

Examples of "**keys**" value:

- "CTRL + R"

- "Z + R + P"

- "3 (NUMPAD)"

- "CTRL + \*"

- "="

Examples of "**link**" value:

- "/about/"

- "http://google.com"

Examples of "**js**" value:

- "alert('HELLO!');"

if for a keyboard combination we have both "**link**" and "**js**" declared, only "**link**" will be condidered.

Another advanced examples for **HOTKEYS** list::

    HOTKEYS = [
                {'keys': 'ctrl+h',  # home
                'link': '/',
                },
                {'keys': 'alt+w',
                'link': '/workspace/',
                },
                {'keys': 'shift+j',
                'js': 'js_function();', # javascript code here
                },
                {'keys': 'a+j',
                'js': 'alert(\'A+J Pressed!\');', # javascript code here
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

The easiest way to do this is to load hotkeys **{% load hotkeys %}** at the **top** of your "base" template and to setup **{% setup_hotkeys %}** the in your **<head>** section.

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


==========================
Do you need some examples?
==========================

Further a list of the most useful keyboard shortcuts of our favorite web services.
So, if you need a suggestion about which key combination use on your site,
this is where you find it:

Gmail
-----

    **c** – compose a new mail

    **/** – puts your cursor in the search box

    **k** – move to newer conversation

    **j** – Move to older conversation

    **n** – next message

    **p** – previous message

    **o or Enter** – open a conversation

    **u** – return to conversation list

    **y** – archive a conversation

    **m** – mute (archive and make all future messages from this conversation
    skip the inbox)
    **x** – select conversation

    **s** – star a message or conversation

    **!** – report spam

    **r** – reply to a mail

    **a** – reply to all recepients

    **f** – forward message

    **Esc** – escape from input field

    **ctrl+s** – save draft


key combos
^^^^^^^^^^

    **tab then Enter** – send message

    **y then o** – archive your conversation and move to the next one.

    **g then a** – go to all mail

    **g then s** – go to starred conversations

    **g then c** – go to contacts list.

    **g then d** – go to drafts

    **g then i** – go to inbox

Google Reader
-------------

    **j/k** – selects the next/previous item in the list

    **space/shift-space** – moves the page down/up

    **n/p** – in list view, selects the next item without opening it

    **o** – in list view, expands or collapses the selected item

    **enter** – in list view, expands or collapses the selected item

    **s** – stars the selected item

    **shift-s** – shares the selected item

    **m** – switches the read state of the selected item

    **t** – opens the tagging field for the selected item

    **v** – opens the original source for this article in a new window

    **shift-a** – marks all items in the current view as read

    **1** – displays the subscription as expanded items

    **2** – displays the subscription as a list of headlines

    **r** – refreshes the unread counts in the navigation

    **shift-n/p** – selects the next/previous subscription or folder in the
    navigation

    **shift-x** – expand or collapse a folder selected in the navigation

    **shift-o** – opens the item currently selected in the navigation

    **gh** – goes to the Google Reader homepage

    **ga** – goes to the “All items” view

    **gs** – goes to the “Starred items” view

    **gt** – allows you to navigate to a tag by entering the tag name

    **gu** – allows you to navigate to a subscription by entering the
    subscription name

    **u** – hides and shows the list of subscriptions

    **?** – displays a quick guide to all of Reader’s shortcuts

Wikipedia
---------

    **+** – add a new section (talk pages only)

    **.** – opens your user page if logged in

    **=** – protect/unprotect the current page (sysops only)

    **c** – shows the content page associated with the current article

    **d** – delete/undelete the current page (sysops only)

    **e** – edit this page/show source of current page

    **f** – search Wikipedia

    **h** – current page’s history

    **j** – shows all of the pages that link to the current one

    **k** – shows recent changes in pages linked to the current one

    **l** – opens your watchlist (logged – in users only)

    **m** – move the current page and its talk page (non – move – protected pages only)

    **n** – opens your user’s or IP’s talk page

    **p** – shows a preview of your changes (on edit pages)

    **q** – shows a list of all special pages

    **r** – shows a list of recent changes to the Wikipedia

    **s** – saves the changes that you have made (on edit pages)

    **t** – opens the current article’s talk page

    **u** – allows you to upload images or media files

    **v** – shows what changes you made to the text (on edit pages)

    **w** – adds the current page to your watchlist (logged – in users only)

    **x** – loads a random article

    **y** – opens a list of your user’s or IP’s contributions

    **z** – goes to the Main Page


Yahoo! Mail
-----------

    **m** – check mail

    **Shift+m** – check all mail

    **Ctrl+** – close current tab

    **n** – new message

    **Shift+n** – new message in its own window

    **r** – reply

    **Shift+r** – reply in a new window

    **a** – reply all

    **Shift+a** – reply all in a new window

    **f** – forward message

    **Shift+f** – forward in a new window

    **k** – mark as read

    **Shift+k** – mark as unread

    **l** – flag

    **Shift+l** – clear flag

    **del** – delete item

    **p/Ctrl+p** – print

    **Ctrl+s** – save draft

    **Ctrl+Enter** – send message

    **v** – turn reading pane on/off

    **Ctrl+[** – navigate through tabs

    **Ctrl+]** – navigate through tabs

    **Enter** – open message in its own tab (when message is selected)

    **Enter** – edit contact info (when contact is selected)

    **Ctrl+f** – find a word or phrase in message

    **F11** – expand window to max height

    **Ctrl+.** – next message (in message tab)

    **Ctrl+,** – previous message (in message tab)

    **Ctrl+Alt+Shift+up arrow/down arrow** – next/previous message

    **Ctrl+Shift+End** – skip to oldest unread message

    **d** – move message to folder

    **Esc** – close read** – message tab

    **Ctrl+Shift+End** – start a new chat


=======
Credits
=======

Special thanks to the authors of this resources:

http://www.w3.org/2002/09/tests/keys.html

http://www.quirksmode.org/js/keys.html#t00

http://unixpapa.com/js/key.html

http://www.openjs.com/scripts/events/keyboard_shortcuts/

https://github.com/jeresig/jquery.hotkeys/

http://mashable.com/2007/06/29/keyboard-shortcuts/


=========
Changelog
=========

0.0.7
-----

* added support for "js" action for your shortcuts
* covered with tests the new functionality
* improved documentation

0.0.6
-----

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