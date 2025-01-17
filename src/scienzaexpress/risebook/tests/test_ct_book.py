# -*- coding: utf-8 -*-
from scienzaexpress.risebook.content.book import IBook  # NOQA E501
from scienzaexpress.risebook.testing import SCIENZAEXPRESS_RISEBOOK_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class BookIntegrationTest(unittest.TestCase):

    layer = SCIENZAEXPRESS_RISEBOOK_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_book_schema(self):
        fti = queryUtility(IDexterityFTI, name='Book')
        schema = fti.lookupSchema()
        self.assertEqual(IBook, schema)

    def test_ct_book_fti(self):
        fti = queryUtility(IDexterityFTI, name='Book')
        self.assertTrue(fti)

    def test_ct_book_factory(self):
        fti = queryUtility(IDexterityFTI, name='Book')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IBook.providedBy(obj),
            u'IBook not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_book_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Book',
            id='book',
        )

        self.assertTrue(
            IBook.providedBy(obj),
            u'IBook not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('book', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('book', parent.objectIds())

    def test_ct_book_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Book')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_book_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Book')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'book_id',
            title='Book container',
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
