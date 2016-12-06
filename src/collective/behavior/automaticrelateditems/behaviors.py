# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope.interface import provider


@provider(IFormFieldProvider)
class IAutomaticRelatedItems(model.Schema):

    """Automatic Related Items behavior."""
