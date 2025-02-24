from plone.api.content import create
from plone.app.contenttypes.content import Folder

import plone.api


def install(context) -> None:
    """Post install script."""
    _setup_utilities_folder(context)


def _setup_utilities_folder(context) -> None:
    """Layout the Utilities folder."""

    def create_folder_if_missing(
        container,
        folder_id: str,
        folder_name: str,
        description: str | None = None,
    ) -> Folder:
        if folder_id not in container:
            folder = create(
                container=container,
                type="Folder",
                id=folder_id,
                title=folder_name,
            )
            if description:
                folder.setDescription(description)
            # 😢 plone.api.portal.show_message(
            # 😢     message=f"Folder {folder_name} created",
            # 😢     request=context.request,
            # 😢     type="warning",
            # 😢 )
            # The above code does not work because
            # ipdb> pp context
            # <SetupTool at /rise/portal_setup>
            # ipdb> pp context.request
            # *** AttributeError: 'RequestContainer' object has no attribute 'request'

            return folder
        else:
            return container.get(folder_id)

    portal = plone.api.portal.get()  # ?
    utilities_folder = create_folder_if_missing(
        portal, "utilities", "Utilities", "Generic utilities"
    )

    subfolders = (
        "template InDesign saggistica",
        "template InDesign manualistica",
        "template InDesign narrativa",
        "template InDesign U Chem",
        "template LaTeX saggistica",
        "template LaTeX manualistica",
        "template LaTeX U Math",
        "manuale di stile per editor e correttori bozze",
        "manuale di stile per autori",
        "manuale di stile per autori NLM",
        "indicazioni grafiche per albi",
    )
    for subfolder in subfolders:
        create_folder_if_missing(
            container=utilities_folder,
            folder_id=subfolder.replace(" ", "_").lower(),
            folder_name=subfolder,
        )
