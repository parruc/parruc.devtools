# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import parruc.devtools


class ParrucDevtoolsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=parruc.devtools)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'parruc.devtools:default')


PARRUC_DEVTOOLS_FIXTURE = ParrucDevtoolsLayer()


PARRUC_DEVTOOLS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PARRUC_DEVTOOLS_FIXTURE,),
    name='ParrucDevtoolsLayer:IntegrationTesting'
)


PARRUC_DEVTOOLS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PARRUC_DEVTOOLS_FIXTURE,),
    name='ParrucDevtoolsLayer:FunctionalTesting'
)


PARRUC_DEVTOOLS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PARRUC_DEVTOOLS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ParrucDevtoolsLayer:AcceptanceTesting'
)
