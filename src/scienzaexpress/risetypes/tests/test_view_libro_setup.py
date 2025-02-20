from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from scienzaexpress.risetypes.testing import SCIENZAEXPRESS_RISETYPES_FUNCTIONAL_TESTING
from scienzaexpress.risetypes.testing import (
    SCIENZAEXPRESS_RISETYPES_INTEGRATION_TESTING,
)
from scienzaexpress.risetypes.views.libro_setup import ILibroSetup
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):
    layer = SCIENZAEXPRESS_RISETYPES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        api.content.create(self.portal, "Folder", "other-folder")
        api.content.create(self.portal, "Document", "front-page")

    def test_libro_setup_is_registered(self):
        view = getMultiAdapter(
            (self.portal["other-folder"], self.portal.REQUEST), name="libro-setup"
        )
        self.assertTrue(ILibroSetup.providedBy(view))

    def test_libro_setup_not_matching_interface(self):
        view_found = True
        try:
            view = getMultiAdapter(
                (self.portal["front-page"], self.portal.REQUEST), name="libro-setup"
            )
        except ComponentLookupError:
            view_found = False
        else:
            view_found = ILibroSetup.providedBy(view)
        self.assertFalse(view_found)


class ViewsFunctionalTest(unittest.TestCase):
    layer = SCIENZAEXPRESS_RISETYPES_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
