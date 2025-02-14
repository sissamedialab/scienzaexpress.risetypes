# scienzaexpress.risetypes

Collection of content types for RISE

## Features

TODO: List our awesome features

## Installation

Install scienzaexpress.risetypes with `pip`:

```shell
pip install scienzaexpress.risetypes
```

And to create the Plone site:

```shell
make create_site
```

## Add features using `plonecli` or `bobtemplates.plone`

This package provides markers as strings (`<!-- extra stuff goes here -->`) that are compatible with [`plonecli`](https://github.com/plone/plonecli) and [`bobtemplates.plone`](https://github.com/plone/bobtemplates.plone).
These markers act as hooks to add all kinds of subtemplates, including behaviors, control panels, upgrade steps, or other subtemplates from `plonecli`.

To run `plonecli` with configuration to target this package, run the following command.

```shell
make add <template_name>
```

For example, you can add a content type to your package with the following command.

```shell
make add content_type
```

You can add a behavior with the following command.

```shell
make add behavior
```

```{seealso}
You can check the list of available subtemplates in the [`bobtemplates.plone` `README.md` file](https://github.com/plone/bobtemplates.plone/?tab=readme-ov-file#provided-subtemplates).
See also the documentation of [Mockup and Patternslib](https://6.docs.plone.org/classic-ui/mockup.html) for how to build the UI toolkit for Classic UI.
```

## Contribute

- [Issue Tracker](https://github.com/gamboz/scienzaexpress.risetypes/issues)
- [Source Code](https://github.com/gamboz/scienzaexpress.risetypes/)

## License

The project is licensed under GPLv2.

## Credits and Acknowledgements 🙏

Generated using [Cookieplone (0.8.1)](https://github.com/plone/cookieplone) and [cookiecutter-plone (91f7d2b)](https://github.com/plone/cookiecutter-plone/commit/91f7d2b0a61b4685d383e79a7367b23b6488e534) on 2025-02-14 15:04:27.612580. A special thanks to all contributors and supporters!
