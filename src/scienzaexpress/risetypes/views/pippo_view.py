from plone.app.contenttypes.browser.file import FileView
from plone.namedfile.interfaces import INamedBlobFile
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse


class PippoView(FileView):
    """Custom view for File content type."""

    def is_pdf(self):
        """Check if the file is a PDF."""
        return self.context.file.contentType == "application/pdf"
