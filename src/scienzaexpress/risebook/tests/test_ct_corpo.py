from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from scienzaexpress.risebook.content.corpo import ICorpo  # NOQA E501
from scienzaexpress.risebook.testing import (  # noqa
    SCIENZAEXPRESS_RISEBOOK_INTEGRATION_TESTING,
)
from zope.component import createObject
from zope.component import queryUtility

import unittest


class CorpoIntegrationTest(unittest.TestCase):
    layer = SCIENZAEXPRESS_RISEBOOK_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            "Book",
            self.portal,
            "parent_container",
            title="Parent container",
        )
        self.parent = self.portal[parent_id]

    def test_ct_corpo_schema(self):
        fti = queryUtility(IDexterityFTI, name="Corpo")
        schema = fti.lookupSchema()
        self.assertEqual(ICorpo, schema)

    def test_ct_corpo_fti(self):
        fti = queryUtility(IDexterityFTI, name="Corpo")
        self.assertTrue(fti)

    def test_ct_corpo_factory(self):
        fti = queryUtility(IDexterityFTI, name="Corpo")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICorpo.providedBy(obj),
            "ICorpo not provided by {}!".format(
                obj,
            ),
        )

    def test_ct_corpo_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.parent,
            type="Corpo",
            id="corpo",
        )

        self.assertTrue(
            ICorpo.providedBy(obj),
            "ICorpo not provided by {}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("corpo", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("corpo", parent.objectIds())

    def test_ct_corpo_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Corpo")
        self.assertFalse(fti.global_allow, f"{fti.id} is globally addable!")

    def test_ct_corpo_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Corpo")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "corpo_id",
            title="Corpo container",
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type="Document",
            title="My Content",
        )
        self.assertTrue(obj, f"Cannot add {obj.id} to {fti.id} container!")
