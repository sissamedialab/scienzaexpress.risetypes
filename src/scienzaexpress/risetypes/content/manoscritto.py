from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IManoscritto(model.Schema):
    """Marker interface and Dexterity Python Schema for Manoscritto."""


@implementer(IManoscritto)
class Manoscritto(Container):
    """Content-type class for IManoscritto."""
