from dataclasses import dataclass
from dataclasses import field
from plone.api.content import create
from typing import List

import keyword
import re


def string_to_identifier(s: str) -> str:
    """
    Convert a string into a valid Python identifier.
    Invalid characters are replaced with underscores.
    If the result is a Python keyword or starts with a digit, it's prefixed.
    """
    # Ugly workaround! 🤮
    # In
    # scienzaexpress.preflights.src.scienzaexpress.preflights.views.validate_pdf_metadata.find_metadata_object
    # we expect the XML folder to have the ID "xml" (lowercase).
    # To correcctly address this we should fix the creation of all XML folders for the old types.
    if s == "XML":
        return "xml"

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
class FolderNode:
    name: str
    subfolders: List["FolderNode"] = field(default_factory=list)
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
