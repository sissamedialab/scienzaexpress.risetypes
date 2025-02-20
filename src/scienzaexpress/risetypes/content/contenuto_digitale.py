from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IContenutoDigitale(model.Schema):
    """Marker interface for ContenutoDigitale"""


@implementer(IContenutoDigitale)
class ContenutoDigitale(Container):
    """Content-type class for IContenutoDigitale"""
