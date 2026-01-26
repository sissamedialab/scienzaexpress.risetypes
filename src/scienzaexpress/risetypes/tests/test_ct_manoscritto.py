# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from scienzaexpress.risetypes.content.manoscritto import IManoscritto  # NOQA E501
from scienzaexpress.risetypes.testing import INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class ManoscrittoIntegrationTest(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_manoscritto_schema(self):
        fti = queryUtility(IDexterityFTI, name="Manoscritto")
        schema = fti.lookupSchema()
        self.assertEqual(IManoscritto, schema)

    def test_ct_manoscritto_fti(self):
        fti = queryUtility(IDexterityFTI, name="Manoscritto")
        self.assertTrue(fti)

    def test_ct_manoscritto_factory(self):
        fti = queryUtility(IDexterityFTI, name="Manoscritto")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IManoscritto.providedBy(obj),
            "IManoscritto not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_manoscritto_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="Manoscritto",
            id="manoscritto",
        )

        self.assertTrue(
            IManoscritto.providedBy(obj),
            "IManoscritto not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("manoscritto", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("manoscritto", parent.objectIds())

    def test_ct_manoscritto_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Manoscritto")
        self.assertTrue(fti.global_allow, "{0} is not globally addable!".format(fti.id))

    def test_ct_manoscritto_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Manoscritto")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "manoscritto_id",
            title="Manoscritto container",
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type="Document",
            title="My Content",
        )
        self.assertTrue(obj, "Cannot add {0} to {1} container!".format(obj.id, fti.id))
