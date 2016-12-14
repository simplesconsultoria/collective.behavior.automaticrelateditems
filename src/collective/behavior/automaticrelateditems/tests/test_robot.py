# -*- coding: utf-8 -*-
from collective.behavior.automaticrelateditems.testing import ROBOT_TESTING
from plone import api
from plone.testing import layered

import os
import robotsuite
import unittest


PLONE_VERSION = api.env.plone_version()


def test_suite():
    suite = unittest.TestSuite()
    current_dir = os.path.abspath(os.path.dirname(__file__))
    tests = [
        doc for doc in os.listdir(current_dir)
        if doc.startswith('test_') and doc.endswith('.robot')
    ]
    # FIXME: skip RobotFramework tests in Plone 5
    if PLONE_VERSION.startswith('5'):
        tests = []
    suite.addTests([
        layered(robotsuite.RobotTestSuite(t), layer=ROBOT_TESTING)
        for t in tests
    ])
    return suite
