from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class INuovaLetteraMatematica(model.Schema):
    """Marker interface for NuovaLetteraMatematica"""


@implementer(INuovaLetteraMatematica)
class NuovaLetteraMatematica(Container):
    """Content-type class for INuovaLetteraMatematica"""
