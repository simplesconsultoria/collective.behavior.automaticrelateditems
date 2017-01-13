# -*- coding: utf-8 -*-
from collective.behavior.autorelateitems.interfaces import IAutoRelateItemsSettings
from collective.behavior.autorelateitems.testing import INTEGRATION_TESTING
from collective.behavior.autorelateitems.utils import get_related
from plone import api

import unittest


class UtilsTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']

        record = dict(name='count', value=2, interface=IAutoRelateItemsSettings)
        api.portal.set_registry_record(**record)

        with api.env.adopt_roles(['Manager']):
            api.content.create(
                container=self.portal,
                type='News Item',
                title='Related Item 1',
                subject=('Tag1'),
            )
            api.content.create(
                container=self.portal,
                type='News Item',
                title='Related Item 2',
                subject=('Tag1', 'Tag2'),
            )
            api.content.create(
                container=self.portal,
                type='News Item',
                title='Related Item 3',
                subject=('Tag1', 'Tag2', 'Tag3'),
            )
            api.content.create(
                container=self.portal,
                type='News Item',
                title='Related Item 4',
                subject=('Tag1', 'Tag2', 'Tag3', 'Tag4'),
            )

    def test_no_tags(self):
        self.assertEqual(get_related([]), [])

    def test_all_tags(self):
        tags = ['Tag1', 'Tag2', 'Tag3', 'Tag4']
        expected = ['/plone/related-item-4', '/plone/related-item-3']
        self.assertEqual(get_related(tags), expected)
