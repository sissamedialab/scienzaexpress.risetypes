# from scienzaexpress.risebook import _
from plone import api
from plone.api.content import create
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
        print("CreatePages called!!!!!!!!")
        # because of the configuration of the view (views/configure.zcml),
        # I should be able to assert isinstance(self.context, Book)

        self.create_cover()
        # TODO: test No need for re-indexing
        # TODO: No need for transitions

        self.create_body()
        # TODO: contratti

        # TODO: add pop-up message or similar: "Book built!"
        # ? # request = container.REQUEST
        # ? # response =  request.response

        # TODO: if all went well, redirect to Book main view

        return self.index()

    def create_cover(self) -> None:
        """Create the container for cover files."""
        if "cover" in self.context:
            api.portal.show_message(
                message="Cover container already exists. Doing nothing!",
                request=self.request,
                type="warning",  # types: 'info', 'warning', 'error', 'success'
            )
            return

        cover = create(
            container=self.context,
            type="Cover",
            id="cover",
            title="Cover",
        )
        cover.setDescription("Cover di mille balene!")

    def create_body(self) -> None:
        """Create the container for body files."""
        if "body" in self.context:
            api.portal.show_message(
                message="Body container already exists. Doing nothing!",
                request=self.request,
                type="warning",  # types: 'info', 'warning', 'error', 'success'
            )
            return

        body = create(
            container=self.context,
            type="Corpo",
            id="body",
            title="Corpo",
        )
        body.setDescription("Corpo di mille balene!")
