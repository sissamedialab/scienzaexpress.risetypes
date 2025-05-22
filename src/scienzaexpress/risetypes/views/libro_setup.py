from dataclasses import dataclass
from dataclasses import field
from plone import api
from plone.api.content import create
from Products.Five.browser import BrowserView
from typing import List
from zope.interface import implementer
from zope.interface import Interface

import keyword
import re


def string_to_identifier(s: str) -> str:
    """
    Convert a string into a valid Python identifier.
    Invalid characters are replaced with underscores.
    If the result is a Python keyword or starts with a digit, it's prefixed.
    """
    # Replace invalid characters with underscores
    identifier = re.sub(r"\W|^(?=\d)", "_", s)

    # Ensure it doesn't start with a digit (already handled by lookahead above)
    # but we'll add an extra prefix if it's a Python keyword
    if keyword.iskeyword(identifier):
        identifier = f"{identifier}_kw"

    # Final fallback if it's empty or just underscores
    if not identifier or identifier.strip("_") == "":
        identifier = "_identifier"

    return identifier


@dataclass
class Folder:
    name: str
    subfolders: List["Folder"] = field(default_factory=list)
    fid: str = field(init=False)

    def __post_init__(self):
        self.fid = string_to_identifier(self.name)

    def create(self, context) -> tuple[list, list]:
        """
        Create this folder and its subfolders starting from the given context.

        Returns a tuple that contains the list of the created folders
        and that of the already existing ones.
        """
        created = []
        existing = []

        if self.fid in context:
            existing.append(self.name)
        else:
            folder = create(
                container=context,
                type="Folder",
                id=self.fid,
                title=self.name,
            )
            folder.setDescription(self.name)
            created.append(self.name)

            for sub in self.subfolders:
                sub_created, sub_existing = sub.create(folder)
                created.extend(sub_created)
                existing.extend(sub_existing)

        return (created, existing)


class ILibroSetup(Interface):
    """Marker Interface for ICreatePages"""


@implementer(ILibroSetup)
class LibroSetup(BrowserView):
    def __call__(self):
        """Setup Libro."""
        # TODO: port to other types
        folders = [
            Folder("ISTRUTTORIA"),
            Folder(
                "PRODUZIONE",
                [
                    Folder("XML"),
                    Folder("Da impaginare per interni"),
                    Folder("Per realizzare la copertina"),
                    Folder("Impaginato interno"),
                    Folder("Copertina impaginata"),
                ],
            ),
            Folder(
                "VISTO SI STAMPI",
                [
                    Folder("Per lo stampatore"),
                    Folder("Per la comunicazione"),
                    Folder("Versione ePub"),
                ],
            ),
            Folder(
                "VITA DEL LIBRO",
                [
                    Folder("Per comunicazione"),
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
