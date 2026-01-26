from plone.app.dexterity.browser.folder_listing import FolderView


class FolderViewNoByline(FolderView):
    """Override FolderView to hide the by-line."""

    @property
    def show_about(self) -> bool:
        """Force the template not to show the by-line."""
        return False
