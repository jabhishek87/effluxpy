.. _builtin-plugins:

Bultin Plugins
==============

A player plugin is provided by default, and more are planned.

Builtin-plugins serve as developers reference, while also being useful for
unit-testing.

.. _builtin-plugins-player:

Player
------

Player plugin provides their own endpoints, widgets and extends both
:class:`effluxpy.file.File` and :class:`effluxpy.file.Directory` so playlists
and directories could be handled.

At the client-side, a slighty tweaked `jPlayer <http://jplayer.org/>`_
implementation is used.

Sources are available at effluxpy's `plugin.player`_ submodule.

.. _plugin.player: https://github.com/jkabhishek/effluxpy/tree/master/effluxpy/plugin/player

.. _builtin-plugins-contributing:

Contributing Builtin Plugins
----------------------------

effluxpy's team is open to contributions of any kind, even about adding
built-in plugins, as long as they comply with the following requirements:

* Plugins must be sufficiently covered by tests to avoid lowering effluxpy's
  overall test coverage.
* Plugins must not add external requirements to effluxpy, optional
  requirements are allowed if plugin can work without them, even with
  limited functionality.
* Plugins should avoid adding specific logic on effluxpy itself, but extending
  effluxpy's itself (specially via plugin interface) in a generic and useful
  way is definitely welcome.

Said that, feel free to fork, code great stuff and fill pull requests at
`GitHub <https://github.com/jkabhishek/effluxpy>`_.
