from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IAlbo(model.Schema):
    """Marker interface for Albo"""


@implementer(IAlbo)
class Albo(Container):
    """Content-type class for IAlbo"""
