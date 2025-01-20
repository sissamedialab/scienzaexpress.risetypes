# from scienzaexpress.risebook import _
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

        # TODO: if exists "cover" then quit

        cover = create(
            container=self.context,
            type="Cover",
            id="cover",
            title="Cover",
        )
        cover.setDescription("Cover di mille balene!")

        # TODO: test No need for re-indexing
        # TODO: No need for transitions

        # TODO: body and contratti

        # TODO: add pop-up message or similar: "Book built!"
        # ? # request = container.REQUEST
        # ? # response =  request.response

        # TODO: if all went well, redirect to Book main view

        return self.index()
