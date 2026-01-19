from ..lib import FolderNode
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class ILibroSetup(Interface):
    """Marker Interface for ICreatePages"""


@implementer(ILibroSetup)
class LibroSetup(BrowserView):
    def __call__(self):
        """Setup Libro."""
        # TODO: port to other types
        folders = [
            FolderNode("ISTRUTTORIA"),
            FolderNode(
                "PRODUZIONE",
                [
                    FolderNode("XML"),
                    FolderNode("Da impaginare per interni"),
                    FolderNode("Per realizzare la copertina"),
                    FolderNode("Impaginato interno"),
                    FolderNode("Copertina impaginata"),
                ],
            ),
            FolderNode(
                "VISTO SI STAMPI",
                [
                    FolderNode("Per lo stampatore"),
                    FolderNode("Per gli add-on"),
                    FolderNode("Per l'e-book"),
                ],
            ),
            FolderNode(
                "VITA DEL LIBRO",
                [
                    FolderNode("Per comunicazione"),
                ],
            ),
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
            message="Libro setup completed.",
            request=self.request,
            type="success",
        )
        return self.index()
