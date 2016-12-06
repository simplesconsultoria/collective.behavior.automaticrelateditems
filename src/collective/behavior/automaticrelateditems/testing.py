# -*- coding: utf-8 -*-
"""Setup testing fixture.

We need to install plone.app.contenttypes always.
"""
from collective.behavior.automaticrelateditems.tests.utils import enable_automatic_related_items_behavior
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE as PLONE_FIXTURE
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.behavior.automaticrelateditems
        self.loadZCML(package=collective.behavior.automaticrelateditems)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'collective.behavior.automaticrelateditems:default')
        enable_automatic_related_items_behavior('News Item')


FIXTURE = Fixture()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name='collective.behavior.automaticrelateditems:Integration')

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name='collective.behavior.automaticrelateditems:Functional')

ROBOT_TESTING = FunctionalTesting(
    bases=(FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name='collective.behavior.automaticrelateditems:Robot',
)
