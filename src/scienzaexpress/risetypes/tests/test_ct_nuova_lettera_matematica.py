from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from scienzaexpress.risetypes.content.nuova_lettera_matematica import (
    INuovaLetteraMatematica,  # NOQA E501
)
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


class NuovaLetteraMatematicaIntegrationTest(unittest.TestCase):
    layer = SCIENZAEXPRESS_RISETYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_nuova_lettera_matematica_schema(self):
        fti = queryUtility(IDexterityFTI, name="Nuova Lettera Matematica")
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName("Nuova Lettera Matematica")
        self.assertIn(schema_name.lstrip("plone_0_"), schema.getName())

    def test_ct_nuova_lettera_matematica_fti(self):
        fti = queryUtility(IDexterityFTI, name="Nuova Lettera Matematica")
        self.assertTrue(fti)

    def test_ct_nuova_lettera_matematica_factory(self):
        fti = queryUtility(IDexterityFTI, name="Nuova Lettera Matematica")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            INuovaLetteraMatematica.providedBy(obj),
            "INuovaLetteraMatematica not provided by {}!".format(
                obj,
            ),
        )

    def test_ct_nuova_lettera_matematica_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="Nuova Lettera Matematica",
            id="nuova_lettera_matematica",
        )

        self.assertTrue(
            INuovaLetteraMatematica.providedBy(obj),
            "INuovaLetteraMatematica not provided by {}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("nuova_lettera_matematica", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("nuova_lettera_matematica", parent.objectIds())

    def test_ct_nuova_lettera_matematica_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Nuova Lettera Matematica")
        self.assertTrue(fti.global_allow, f"{fti.id} is not globally addable!")

    def test_ct_nuova_lettera_matematica_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Nuova Lettera Matematica")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "nuova_lettera_matematica_id",
            title="Nuova Lettera Matematica container",
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type="Document",
            title="My Content",
        )
        self.assertTrue(obj, f"Cannot add {obj.id} to {fti.id} container!")
