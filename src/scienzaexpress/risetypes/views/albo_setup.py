from ..lib import FolderNode
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class IAlboSetup(Interface):
    """Marker Interface for ICreatePages"""


@implementer(IAlboSetup)
class AlboSetup(BrowserView):
    def __call__(self):
        """Setup Albo."""
        folders = [
            FolderNode("cartella InDesign interni"),
            FolderNode("cartella InDesign copertina"),
            FolderNode("cartella InDesign risguardi"),
            FolderNode("testo definitivo da impaginare"),
            FolderNode("pdf interattivo interno"),
            FolderNode("pdf interattivo copertina"),
            FolderNode("pdf esecutivo per stampa interno"),
            FolderNode("pdf esecutivo per stampa copertina"),
            FolderNode("pdf esecutivo per stampa risguardi"),
            FolderNode("prima di copertina"),
            FolderNode("foto autore"),
            FolderNode("scheda librai"),
            FolderNode("scheda stampa"),
            FolderNode("specimen"),
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
            message="Albo setup completed.",
            request=self.request,
            type="success",
        )
        return self.index()
