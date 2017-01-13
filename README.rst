***********************************
Support for Automatic Related Items
***********************************

.. contents:: Table of Contents

Life, the Universe, and Everything
==================================

A behavior for Dexterity-based content types to add a button to automatically fill related items based on shared tags.

Mostly Harmless
===============

.. image:: http://img.shields.io/pypi/v/collective.behavior.autorelateitems.svg
   :target: https://pypi.python.org/pypi/collective.behavior.autorelateitems

.. image:: https://img.shields.io/travis/collective/collective.behavior.autorelateitems/master.svg
    :target: http://travis-ci.org/collective/collective.behavior.autorelateitems

.. image:: https://img.shields.io/coveralls/collective/collective.behavior.autorelateitems/master.svg
    :target: https://coveralls.io/r/collective/collective.behavior.autorelateitems

Got an idea? Found a bug? Let us know by `opening a support ticket <https://github.com/collective/collective.behavior.autorelateitems/issues>`_.

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
        collective.behavior.autorelateitems

After updating the configuration you need to run ''bin/buildout'', which will take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``Support for Automatic Related Items`` and click the 'Activate' button.

Usage
-----

To use this behaviour you need to also enable Related Items behavior in your content type.

How does it work
----------------

When you fire the button to load related items, it will search for all the items with more similar tags, and fill the related items automatically.

To calculate the similar tags, this package do one search for each tag, and sum how many times the item appear at the searches. The item that appear more are the item with more similar tags.

The amount of items filled are configured into a controlpanel option.

Not entirely unlike
===================

`fourdigits.portlet.keywordrelated <https://pypi.python.org/pypi/fourdigits.portlet.keywordrelated>`_
    This product gives you a new portlet: the KeywordRelatedPortlet.
    It shows other content in the site that has the same tags as the current page.

`collective.simserver.related <https://github.com/collective/collective.simserver.related>`_
    collective.simserver.related provides a form to query the simserver for similar items and set them as related items.
    A simserver collection queries the simserver for all documents related to this collection.
    More information at: https://github.com/collective/collective.simserver.core

`collective.relatedslider <https://github.com/collective/collective.relatedslider>`_
    This is a Plone addon that adds a behavior and viewlet for displaying related content in a scrollable slider at the bottom of the content area.
    It can use either the relatedItems behavior or collection behavior applied to the content for determining the related items.

`collective.portlet.relateditems <https://pypi.python.org/pypi/collective.portlet.relateditems>`_
    This is a simple portlet that displays content similar to the present context.
    Related items are compiled based on the context title and keywords.
    In case of a folderish context related items are computed based on the contents of the folder and the folder information.
