# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class IManoscrittoSetup(Interface):
    """Marker Interface for IManoscrittoSetup"""


@implementer(IManoscrittoSetup)
class ManoscrittoSetup(BrowserView):
    def __call__(self):
        template = """<li class="heading" i18n:translate="">
          Sample View
        </li>"""
        return template
