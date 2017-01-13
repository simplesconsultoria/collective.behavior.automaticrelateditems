# -*- coding: utf-8 -*-
from collective.behavior.autorelateitems import _
from collective.behavior.autorelateitems.interfaces import IAutoRelateItemsSettings
from plone.app.registry.browser import controlpanel


class AutoRelateItemsSettingsEditForm(controlpanel.RegistryEditForm):

    """Control panel edit form."""

    schema = IAutoRelateItemsSettings
    label = _(u'Auto Relate Items')
    description = _(u'Settings for Automatic Related Items.')


class AutoRelateItemsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):

    """Control panel form wrapper."""

    form = AutoRelateItemsSettingsEditForm
