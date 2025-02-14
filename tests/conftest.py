from pytest_plone import fixtures_factory
from scienzaexpress.risetypes.testing import ACCEPTANCE_TESTING
from scienzaexpress.risetypes.testing import FUNCTIONAL_TESTING
from scienzaexpress.risetypes.testing import INTEGRATION_TESTING


pytest_plugins = ["pytest_plone"]


globals().update(
    fixtures_factory(
        (
            (ACCEPTANCE_TESTING, "acceptance"),
            (FUNCTIONAL_TESTING, "functional"),
            (INTEGRATION_TESTING, "integration"),
        )
    )
)
