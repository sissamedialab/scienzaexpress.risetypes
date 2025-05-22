from ..lib import FolderNode
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class IScireSetup(Interface):
    """Marker Interface for ICreatePages"""


@implementer(IScireSetup)
class ScireSetup(BrowserView):
    def __call__(self):
        """Setup SCIRE."""
        folders = [
            FolderNode("cartella InDesign interni"),
            FolderNode("cartella InDesign copertina"),
            FolderNode("pdf interattivo interno"),
            FolderNode("pdf interattivo copertina"),
            FolderNode("pdf esecutivo per stampa interno"),
            FolderNode("pdf esecutivo per stampa copertina"),
            FolderNode("prima di copertina"),
            FolderNode("scheda librai"),
            FolderNode("scheda stampa"),
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
            message="SCIRE setup completed.",
            request=self.request,
            type="success",
        )
        return self.index()
