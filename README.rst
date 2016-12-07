*******************************
Automatic Related Items Support
*******************************

.. contents:: Table of Contents

Life, the Universe, and Everything
==================================

A behavior for Dexterity-based content types to add a button to automatically fill related items based on Tags.

Mostly Harmless
===============

.. image:: http://img.shields.io/pypi/v/collective.behavior.automaticrelateditems.svg
   :target: https://pypi.python.org/pypi/collective.behavior.automaticrelateditems

.. image:: https://img.shields.io/travis/collective/collective.behavior.automaticrelateditems/master.svg
    :target: http://travis-ci.org/collective/collective.behavior.automaticrelateditems

.. image:: https://img.shields.io/coveralls/collective/collective.behavior.automaticrelateditems/master.svg
    :target: https://coveralls.io/r/collective/collective.behavior.automaticrelateditems

Got an idea? Found a bug? Let us know by `opening a support ticket <https://github.com/collective/collective.behavior.automaticrelateditems/issues>`_.

Don't Panic
===========

Installation
------------

To enable this package in a buildout-based installation:

#. Edit your buildout.cfg and add add the following to it:

.. code-block:: ini

    [buildout]
    ...
    eggs =
        collective.behavior.automaticrelateditems

After updating the configuration you need to run ''bin/buildout'', which will take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``Automatic Related Items Support`` and click the 'Activate' button.

Usage
-----

To use this behaviour you need to also enable Related Items behavior in your content type.

How does it work
----------------

When you fire the button to load related items, it will search for all the items with more similar tags, and fill the related items automatically.

To calculate the similar tags, this package do one search for each tag, and sum how many times the item appear at the searches. The item that appear more are the item with more similar tags.

The amount of items filled are configured into a controlpanel option.
