from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ILibro(model.Schema):
    """Marker interface for Libro"""


@implementer(ILibro)
class Libro(Container):
    """Content-type class for ILibro"""
