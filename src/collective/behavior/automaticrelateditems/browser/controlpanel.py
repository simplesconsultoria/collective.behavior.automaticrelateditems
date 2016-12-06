# -*- coding: utf-8 -*-
from collective.behavior.automaticrelateditems import _
from collective.behavior.automaticrelateditems.interfaces import IAutomaticRelatedItemsSettings
from plone.app.registry.browser import controlpanel


class AutomaticRelatedItemsSettingsEditForm(controlpanel.RegistryEditForm):

    """Control panel edit form."""

    schema = IAutomaticRelatedItemsSettings
    label = _(u'Automatic Related Items')
    description = _(u'Settings for Automatic Related Items.')


class AutomaticRelatedItemsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):

    """Control panel form wrapper."""

    form = AutomaticRelatedItemsSettingsEditForm
