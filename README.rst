*******
Manager
*******

What is hopefully going to be a *very* simple package manager to install modules from ABC and make sure interdependencies are met.

----

To help make ABC as absolutely easy as possible to use, the hope is to offer a *very simple* package manager to add ABC modules to C projects and manage the interdependencies between ABC modules.

The package manager should be incredibly easy to use, verbose, and try to assist the user as much as possible by helping them to avoid any mistakes that could easily arise. Examples of mistakes it should hopefully be able to gracefully handle:

- Dependancies between ABC modules
- Project file structure
- Removing ABC modules without breaking dependancies
- Updating ABC modules, checking dependancies
- ABC manager should be runnable from any directory on the computer with appropriate permissions.

Things ABC manager will not handle:

- 3rd party packages
- Automatic updating of modules
- Managing user code

ABC Manager is **NOT** intended to be the primary way to use ABC modules. It is simply provided as a means to quickly get up and running with ABC modules, however ABC modules should be easily installed on their own without the need of the manager.