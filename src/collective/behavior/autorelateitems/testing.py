# -*- coding: utf-8 -*-
"""Setup testing fixture.

We need to install plone.app.contenttypes always.
"""
from collective.behavior.autorelateitems.tests.utils import enable_automatic_related_items_behavior
from collective.behavior.autorelateitems.tests.utils import enable_related_items_behavior
from plone import api
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE as PLONE_FIXTURE
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2


IS_PLONE_5 = api.env.plone_version().startswith('5')


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.behavior.autorelateitems
        self.loadZCML(package=collective.behavior.autorelateitems)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'collective.behavior.autorelateitems:default')
        enable_related_items_behavior('News Item')
        enable_automatic_related_items_behavior('News Item')
        portal.portal_workflow.setDefaultChain('one_state_workflow')


FIXTURE = Fixture()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name='collective.behavior.autorelateitems:Integration')

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name='collective.behavior.autorelateitems:Functional')

ROBOT_TESTING = FunctionalTesting(
    bases=(FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name='collective.behavior.autorelateitems:Robot',
)
