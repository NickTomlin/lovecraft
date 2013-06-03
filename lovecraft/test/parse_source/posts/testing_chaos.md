Title: The definitive guide to testing despair. Python edition.
---

Ah testing. Such a lovely idea; such a simple idea. Unfortunately it is not as easy to start as a beginner.

Python's built in UnitTest module seems a wonderful start, until you run into issues with modules and importing.
It seem like this is not an easy concept, by the number of Posts on stackoverflow. I'm still struggling with it myself,


The options are:

- [#1 Use relative imports](http://stackoverflow.com/a/714647/1048479) ``from ... import foo`` (only works within a package, did not work with nose)
- [#2 Alter the system path](http://stackoverflow.com/a/11158224/1048479):

    ```
    import os,sys
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0,parentdir)
    import mymodule
    ```
- [#3 Remove the __init__.py and just use import](http://stackoverflow.com/a/3073368/1048479). This is for simpler non-package testing. Still trying to figure out what the detriment is.


# Printing with Nose

``nosetests --nocapture`` will allow print() output to show up in your testing logs. Useful for beginners like me. This can be speicfied in a global noseconfig file in your HOME directory. @todo: create nose file :)

## Note, don't be stupid like me
I was further struggling with imports within my package, when I realized that my directory name contained dashes (``my-cool-folder``) which is a no-no as far as Python is concerned. Changing the dashes to underscores cleared up those issues. Only took a day to figure out :)

## Big Ol' List of helpful threads

- [#1 Where do the Python Unit Tests go?](http://stackoverflow.com/questions/61151/where-do-the-python-unit-tests-go)
- [#2 Import Module from a Folder](http://stackoverflow.com/questions/279237/python-import-a-module-from-a-folder?rq=1)
- [#3 (mentions 4 methods!) Importing modules from parent folder ](http://stackoverflow.com/questions/714063/python-importing-modules-from-parent-folder?rq=1)
