from ..lib import FolderNode
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class IContenutoDigitaleSetup(Interface):
    """Marker Interface for ICreatePages"""


@implementer(IContenutoDigitaleSetup)
class ContenutoDigitaleSetup(BrowserView):
    def __call__(self):
        """Setup Contenuto Digitale."""
        folders = [
            FolderNode("immagine di copertina"),
            FolderNode("testo"),
            FolderNode("repository con immagini e multimedia"),
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
            message="Contenuto Digitale setup completed.",
            request=self.request,
            type="success",
        )
        return self.index()
