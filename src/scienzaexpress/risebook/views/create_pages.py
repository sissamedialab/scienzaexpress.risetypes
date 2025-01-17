# from scienzaexpress.risebook import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ICreatePages(Interface):
    """Marker Interface for ICreatePages"""


@implementer(ICreatePages)
class CreatePages(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('create_pages.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
