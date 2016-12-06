# -*- coding: utf-8 -*-
from collective.behavior.automaticrelateditems.config import PROJECTNAME
from collective.behavior.automaticrelateditems.interfaces import IAutomaticRelatedItemsSettings
from collective.behavior.automaticrelateditems.testing import INTEGRATION_TESTING
from plone import api
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import unittest


class ControlPanelTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.controlpanel = self.portal['portal_controlpanel']

    def test_controlpanel_has_view(self):
        view = api.content.get_view(u'automaticrelateditems-settings', self.portal, self.request)
        view = view.__of__(self.portal)
        self.assertTrue(view())

    def test_controlpanel_view_is_protected(self):
        from AccessControl import Unauthorized
        from plone.app.testing import logout
        logout()
        with self.assertRaises(Unauthorized):
            self.portal.restrictedTraverse('@@automaticrelateditems-settings')

    def test_controlpanel_installed(self):
        actions = [
            a.getAction(self)['id'] for a in self.controlpanel.listActions()]
        self.assertIn('automaticrelateditems', actions)

    def test_controlpanel_removed_on_uninstall(self):
        qi = self.portal['portal_quickinstaller']

        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=[PROJECTNAME])

        actions = [
            a.getAction(self)['id'] for a in self.controlpanel.listActions()]
        self.assertNotIn('automaticrelateditems', actions)


class RegistryTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.registry = getUtility(IRegistry)
        self.settings = self.registry.forInterface(IAutomaticRelatedItemsSettings)

    def test_count_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'count'))
        self.assertEqual(self.settings.count, 5)

    def test_records_removed_on_uninstall(self):
        qi = self.portal['portal_quickinstaller']
        qi.uninstallProducts(products=[PROJECTNAME])

        records = [
            IAutomaticRelatedItemsSettings.__identifier__ + '.count',
        ]

        for r in records:
            self.assertNotIn(r, self.registry)
