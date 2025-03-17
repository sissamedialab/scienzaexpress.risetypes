from plone import api
from plone.api.content import create
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IEBookSetup(Interface):
    """Marker Interface for ICreatePages"""


@implementer(IEBookSetup)
class EBookSetup(BrowserView):
    def __call__(self):
        """Setup E-Book."""

        if "copertina_interno" in self.context:
            api.portal.show_message(
                message="copertina+interno already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="copertina_interno",
                title="copertina+interno",
            )
            subfolder.setDescription("copertina+interno")

        if "isbn_codice_a_barre" in self.context:
            api.portal.show_message(
                message="ISBN codice a barre already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="isbn_codice_a_barre",
                title="ISBN codice a barre",
            )
            subfolder.setDescription("ISBN codice a barre (jpg, pdf, eps)")

        if "xml" in self.context:
            api.portal.show_message(
                message="La cartella XML esiste già. Niente da fare!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="xml",
                title="XML",
            )
            subfolder.setDescription("Metadata e contenuti XML")

        api.portal.show_message(
            message="E-Book setup completed.",
            request=self.request,
            type="success",
        )
        return self.index()
