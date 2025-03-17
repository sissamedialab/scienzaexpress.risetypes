from plone import api
from plone.api.content import create
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IMaterialeIstruttorioSetup(Interface):
    """Marker Interface for ICreatePages"""


@implementer(IMaterialeIstruttorioSetup)
class MaterialeIstruttorioSetup(BrowserView):
    def __call__(self):
        """Setup Materiale Istruttorio."""

        if "contratto_autore" in self.context:
            api.portal.show_message(
                message="contratto autore already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="contratto_autore",
                title="contratto autore",
            )
            subfolder.setDescription("contratto autore")

        if "testo_da_autori" in self.context:
            api.portal.show_message(
                message="testo da autori already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="testo_da_autori",
                title="testo da autori",
            )
            subfolder.setDescription("testo da autori")

        if "cartella_figure_da_autori" in self.context:
            api.portal.show_message(
                message="cartella figure da autori already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="cartella_figure_da_autori",
                title="cartella figure da autori",
            )
            subfolder.setDescription("cartella figure da autori")

        if "materiale_digitale_da_autori" in self.context:
            api.portal.show_message(
                message="materiale digitale da autori already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="materiale_digitale_da_autori",
                title="materiale digitale da autori",
            )
            subfolder.setDescription("materiale digitale da autori")

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
            message="Materiale Istruttorio setup completed.",
            request=self.request,
            type="success",
        )
        return self.index()
