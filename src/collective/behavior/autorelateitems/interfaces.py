# -*- coding: utf-8 -*-
from collective.behavior.autorelateitems import _
from plone.supermodel import model
from zope import schema
from zope.interface import Interface


class IAddOnLayer(Interface):
    """A layer specific for this add-on product."""


class IAutoRelateItemsSettings(model.Schema):
    """Schema for the control panel form."""

    count = schema.Int(
        title=_(u'Count'),
        description=_(u'Number of related items to be added automatically.'),
        required=True,
        default=5,
        min=1,
        max=5,
    )
