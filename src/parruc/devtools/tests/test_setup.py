# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from parruc.devtools.testing import PARRUC_DEVTOOLS_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that parruc.devtools is properly installed."""

    layer = PARRUC_DEVTOOLS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if parruc.devtools is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'parruc.devtools'))

    def test_browserlayer(self):
        """Test that IParrucDevtoolsLayer is registered."""
        from parruc.devtools.interfaces import (
            IParrucDevtoolsLayer)
        from plone.browserlayer import utils
        self.assertIn(IParrucDevtoolsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PARRUC_DEVTOOLS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['parruc.devtools'])

    def test_product_uninstalled(self):
        """Test if parruc.devtools is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'parruc.devtools'))

    def test_browserlayer_removed(self):
        """Test that IParrucDevtoolsLayer is removed."""
        from parruc.devtools.interfaces import IParrucDevtoolsLayer
        from plone.browserlayer import utils
        self.assertNotIn(IParrucDevtoolsLayer, utils.registered_layers())
