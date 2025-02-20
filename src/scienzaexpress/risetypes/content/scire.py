from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IScire(model.Schema):
    """Marker interface for Scire"""


@implementer(IScire)
class Scire(Container):
    """Content-type class for IScire"""
