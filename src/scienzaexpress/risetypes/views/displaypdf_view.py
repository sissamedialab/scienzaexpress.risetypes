from plone.app.contenttypes.browser.file import FileView
from plone.namedfile.interfaces import INamedBlobFile
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse


class DisplayPDFView(FileView):
    """View that tells is a File is a pdf."""

    def is_pdf(self) -> bool:
        """Check if the file is a PDF."""
        return self.context.file.contentType == "application/pdf"
