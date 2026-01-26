from ..lib import FolderNode
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IEBookSetup(Interface):
    """Marker Interface for ICreatePages."""


@implementer(IEBookSetup)
class EBookSetup(BrowserView):
    def __call__(self):
        """Set up E-Book."""
        folders = [
            FolderNode("copertina+interno"),
            FolderNode("ISBN codice a barre"),
            FolderNode("XML"),
        ]

        # We don't have a "root" but must work on a list
        created = []
        existing = []
        for folder in folders:
            sub_created, sub_existing = folder.create(self.context)
            created.extend(sub_created)
            existing.extend(sub_existing)

        # Report a warning for each folder that already existed.
        # No need to say anything about created ones.
        for folder in existing:
            api.portal.show_message(
                message=f'la cartella "{folder}" esiste già.',
                request=self.request,
                type="warning",
            )

        api.portal.show_message(
            message="E-Book setup completed.",
            request=self.request,
            type="success",
        )
        return self.request.response.redirect(self.context.absolute_url())
