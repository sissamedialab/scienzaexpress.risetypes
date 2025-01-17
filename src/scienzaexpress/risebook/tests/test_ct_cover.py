# -*- coding: utf-8 -*-
from scienzaexpress.risebook.content.cover import ICover  # NOQA E501
from scienzaexpress.risebook.testing import SCIENZAEXPRESS_RISEBOOK_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class CoverIntegrationTest(unittest.TestCase):

    layer = SCIENZAEXPRESS_RISEBOOK_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Book',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_cover_schema(self):
        fti = queryUtility(IDexterityFTI, name='Cover')
        schema = fti.lookupSchema()
        self.assertEqual(ICover, schema)

    def test_ct_cover_fti(self):
        fti = queryUtility(IDexterityFTI, name='Cover')
        self.assertTrue(fti)

    def test_ct_cover_factory(self):
        fti = queryUtility(IDexterityFTI, name='Cover')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICover.providedBy(obj),
            u'ICover not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_cover_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Cover',
            id='cover',
        )

        self.assertTrue(
            ICover.providedBy(obj),
            u'ICover not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('cover', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('cover', parent.objectIds())

    def test_ct_cover_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Cover')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_cover_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Cover')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'cover_id',
            title='Cover container',
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
