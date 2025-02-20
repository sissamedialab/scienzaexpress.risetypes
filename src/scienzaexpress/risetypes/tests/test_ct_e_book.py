from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from scienzaexpress.risetypes.content.e_book import IEBook  # NOQA E501
from scienzaexpress.risetypes.testing import (  # noqa
    SCIENZAEXPRESS_RISETYPES_INTEGRATION_TESTING,
)
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class EBookIntegrationTest(unittest.TestCase):
    layer = SCIENZAEXPRESS_RISETYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_e_book_schema(self):
        fti = queryUtility(IDexterityFTI, name="E-Book")
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName("E-Book")
        self.assertIn(schema_name.lstrip("plone_0_"), schema.getName())

    def test_ct_e_book_fti(self):
        fti = queryUtility(IDexterityFTI, name="E-Book")
        self.assertTrue(fti)

    def test_ct_e_book_factory(self):
        fti = queryUtility(IDexterityFTI, name="E-Book")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IEBook.providedBy(obj),
            "IEBook not provided by {}!".format(
                obj,
            ),
        )

    def test_ct_e_book_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="E-Book",
            id="e_book",
        )

        self.assertTrue(
            IEBook.providedBy(obj),
            "IEBook not provided by {}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("e_book", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("e_book", parent.objectIds())

    def test_ct_e_book_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="E-Book")
        self.assertTrue(fti.global_allow, f"{fti.id} is not globally addable!")

    def test_ct_e_book_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="E-Book")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "e_book_id",
            title="E-Book container",
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type="Document",
            title="My Content",
        )
        self.assertTrue(obj, f"Cannot add {obj.id} to {fti.id} container!")
