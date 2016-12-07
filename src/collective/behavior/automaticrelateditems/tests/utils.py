# -*- coding: utf-8 -*-
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import queryUtility


def enable_related_items_behavior(portal_type):
    """Enable Related Items behavior on the specified portal type."""
    fti = queryUtility(IDexterityFTI, name=portal_type)
    behavior = 'plone.app.relationfield.behaviors.IRelatedItems'
    if behavior in fti.behaviors:
        return
    behaviors = list(fti.behaviors)
    behaviors.append(behavior)
    fti.behaviors = tuple(behaviors)


def enable_automatic_related_items_behavior(portal_type):
    """Enable Automatic Related Items behavior on the specified portal type."""
    fti = queryUtility(IDexterityFTI, name=portal_type)
    behavior = 'collective.behavior.automaticrelateditems.behaviors.IAutomaticRelatedItems'
    if behavior in fti.behaviors:
        return
    behaviors = list(fti.behaviors)
    behaviors.append(behavior)
    fti.behaviors = tuple(behaviors)
