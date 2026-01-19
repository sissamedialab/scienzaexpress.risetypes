from plone.namedfile.browser import Download
from zope.publisher.interfaces import NotFound


class DisplayFile(Download):
    """Serve file inline (for PDF viewing in browser)."""

    def set_headers(self, file) -> None:
        """Force content disposition to "inline"."""
        super().set_headers(file)
        self.request.response.setHeader("Content-Disposition", "inline")
