from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class IMaterialeIstruttorio(model.Schema):
    """Marker interface for MaterialeIstruttorio"""


@implementer(IMaterialeIstruttorio)
class MaterialeIstruttorio(Container):
    """Content-type class for IMaterialeIstruttorio"""
