from plone import api
from plone.api.content import create
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IContenutoDigitaleSetup(Interface):
    """Marker Interface for ICreatePages"""


@implementer(IContenutoDigitaleSetup)
class ContenutoDigitaleSetup(BrowserView):
    def __call__(self):
        """Setup Contenuto Digitale."""

        if "immagine_di_copertina" in self.context:
            api.portal.show_message(
                message="immagine di copertina already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="immagine_di_copertina",
                title="immagine di copertina",
            )
            subfolder.setDescription("immagine di copertina")

        if "testo" in self.context:
            api.portal.show_message(
                message="testo already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="testo",
                title="testo",
            )
            subfolder.setDescription("testo (o altro file)")

        if "repository_con_immagini_e_multimedia" in self.context:
            api.portal.show_message(
                message="repository con immagini e multimedia already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="repository_con_immagini_e_multimedia",
                title="repository con immagini e multimedia",
            )
            subfolder.setDescription("repository con immagini e multimedia")

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
            message="Contenuto Digitale setup completed.",
            request=self.request,
            type="success",
        )
        return self.index()
