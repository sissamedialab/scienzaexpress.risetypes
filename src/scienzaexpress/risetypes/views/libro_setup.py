from plone import api
from plone.api.content import create
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ILibroSetup(Interface):
    """Marker Interface for ICreatePages"""


@implementer(ILibroSetup)
class LibroSetup(BrowserView):
    def __call__(self):
        """Setup Libro."""

        if "cartella_indesign_latex_interni" in self.context:
            api.portal.show_message(
                message="cartella InDesign/LaTeX interni already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="cartella_indesign_latex_interni",
                title="cartella InDesign/LaTeX interni",
            )
            subfolder.setDescription("cartella InDesign/LaTeX interni")

        if "cartella_indesign_copertina" in self.context:
            api.portal.show_message(
                message="cartella InDesign copertina already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="cartella_indesign_copertina",
                title="cartella InDesign copertina",
            )
            subfolder.setDescription("cartella InDesign copertina")

        if "testo_definitivo_da_impaginare" in self.context:
            api.portal.show_message(
                message="testo definitivo da impaginare already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="testo_definitivo_da_impaginare",
                title="testo definitivo da impaginare",
            )
            subfolder.setDescription("testo definitivo da impaginare (word, LaTeX)")

        if "cartella_figure_definitive_da_impaginare" in self.context:
            api.portal.show_message(
                message="cartella figure definitive da impaginare already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="cartella_figure_definitive_da_impaginare",
                title="cartella figure definitive da impaginare",
            )
            subfolder.setDescription(
                "cartella figure definitive da impaginare (png, pdf, eps, …)"
            )

        if "pdf_interattivo_interno" in self.context:
            api.portal.show_message(
                message="pdf interattivo interno already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="pdf_interattivo_interno",
                title="pdf interattivo interno",
            )
            subfolder.setDescription("pdf interattivo interno")

        if "pdf_interattivo_copertina" in self.context:
            api.portal.show_message(
                message="pdf interattivo copertina already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="pdf_interattivo_copertina",
                title="pdf interattivo copertina",
            )
            subfolder.setDescription("pdf interattivo copertina")

        if "pdf_esecutivo_per_stampa_interno" in self.context:
            api.portal.show_message(
                message="pdf esecutivo per stampa interno already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="pdf_esecutivo_per_stampa_interno",
                title="pdf esecutivo per stampa interno",
            )
            subfolder.setDescription("pdf esecutivo per stampa interno")

        if "pdf_esecutivo_per_stampa_copertina" in self.context:
            api.portal.show_message(
                message="pdf esecutivo per stampa copertina already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="pdf_esecutivo_per_stampa_copertina",
                title="pdf esecutivo per stampa copertina",
            )
            subfolder.setDescription("pdf esecutivo per stampa copertina")

        if "prima_di_copertina" in self.context:
            api.portal.show_message(
                message="prima di copertina already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="prima_di_copertina",
                title="prima di copertina",
            )
            subfolder.setDescription("prima di copertina (jpg)")

        if "foto_autore" in self.context:
            api.portal.show_message(
                message="foto autore already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="foto_autore",
                title="foto autore",
            )
            subfolder.setDescription("foto autore (jpg, png)")

        if "scheda_librai" in self.context:
            api.portal.show_message(
                message="scheda librai already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="scheda_librai",
                title="scheda librai",
            )
            subfolder.setDescription("scheda librai (pdf)")

        if "scheda_stampa" in self.context:
            api.portal.show_message(
                message="scheda stampa already exists. Doing nothing!",
                request=self.request,
                type="warning",
            )
        else:
            subfolder = create(
                container=self.context,
                type="Folder",
                id="scheda_stampa",
                title="scheda stampa",
            )
            subfolder.setDescription("scheda stampa (pdf)")

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
            message="Libro setup completed.",
            request=self.request,
            type="success",
        )
        return self.index()
