from plone.namedfile.browser import Download
from zope.publisher.interfaces import NotFound


class DisplayFile(Download):
    """Serve file inline (for PDF viewing in browser)."""

    def __call__(self):
        file = self._getFile()
        if file is None:
            raise NotFound(self, self.fieldname, self.request)
        import pdb

        pdb.set_trace()
        self.set_headers(file)
        # Override Content-Disposition to inline instead of attachment
        filename = getattr(file, "filename", self.fieldname)
        self.request.response.setHeader(
            "Content-Disposition", f'inline; filename="{filename}XXX"'
        )
        return super().__call__()
