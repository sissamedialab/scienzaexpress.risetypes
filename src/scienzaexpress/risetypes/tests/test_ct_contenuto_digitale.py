from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from scienzaexpress.risetypes.content.contenuto_digitale import (
    IContenutoDigitale,  # NOQA E501
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


class ContenutoDigitaleIntegrationTest(unittest.TestCase):
    layer = SCIENZAEXPRESS_RISETYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_contenuto_digitale_schema(self):
        fti = queryUtility(IDexterityFTI, name="Contenuto Digitale")
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName("Contenuto Digitale")
        self.assertIn(schema_name.lstrip("plone_0_"), schema.getName())

    def test_ct_contenuto_digitale_fti(self):
        fti = queryUtility(IDexterityFTI, name="Contenuto Digitale")
        self.assertTrue(fti)

    def test_ct_contenuto_digitale_factory(self):
        fti = queryUtility(IDexterityFTI, name="Contenuto Digitale")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IContenutoDigitale.providedBy(obj),
            "IContenutoDigitale not provided by {}!".format(
                obj,
            ),
        )

    def test_ct_contenuto_digitale_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="Contenuto Digitale",
            id="contenuto_digitale",
        )

        self.assertTrue(
            IContenutoDigitale.providedBy(obj),
            "IContenutoDigitale not provided by {}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("contenuto_digitale", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("contenuto_digitale", parent.objectIds())

    def test_ct_contenuto_digitale_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Contenuto Digitale")
        self.assertTrue(fti.global_allow, f"{fti.id} is not globally addable!")

    def test_ct_contenuto_digitale_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Contenuto Digitale")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "contenuto_digitale_id",
            title="Contenuto Digitale container",
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type="Document",
            title="My Content",
        )
        self.assertTrue(obj, f"Cannot add {obj.id} to {fti.id} container!")
