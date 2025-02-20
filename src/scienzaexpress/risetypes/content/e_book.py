from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IEBook(model.Schema):
    """Marker interface for EBook"""


@implementer(IEBook)
class EBook(Container):
    """Content-type class for IEBook"""
