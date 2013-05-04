title: two minute guide to virtual environments in python
category: nuts and bolts
tags: venv, virtualenvwrapper
---

I approached virtual environments with the same attitude I originally aprroached VCS's like Git: distrust. But, after experiencing the freedom to mix and match packages and package versions without the fear of conflicts, and to deploy easily to platforms like Heroku, I can't start a project without them.

# Gettting up and running
First of all, if you do not have [PyPi / Pip](https://pypi.python.org/pypi/pip) installed, you should go and do so. It makes installing python packages easy and fun, and conjures up memories of [Charles Dickens](https://en.wikipedia.org/wiki/Charles_Dickens). Don't tell anyone, but Sometimes I say the package names in English accents for fun when I install them with Pip.

To make a long story short, you should use [virtualenvburrito](https://github.com/brainsik/virtualenv-burrito). It's the simplest way to get up and running, and has a lot of nerd cred right now so you can feel cool about yourself (I did). It will install [virtualenv](http://www.virtualenv.org/en/latest/) and [virtualenvwrapper](https://bitbucket.org/dhellmann/virtualenvwrapper) in one easy shell command. Due not that if you __do__ have virtualenv installed already, you may want to manually install virtualenvwrapper yourself; i've done it both ways without a noticeable difference, but better safe than sorry : )

# Cheat Sheet:

- Creating a new Virtual Environment
-- ``mkvirtualenv <env-name>``

- Switching environemnt
-- ``workon <env-name>``

- Checking packages
-- ``lssitepackages``

- Exporting packages
-- ``lssitepackages > requirements.txt``
-- To use in another environment:
--- ``makvirtualenv <env-name> -r path/to/requirements.txt``


# Rant

Virtualenv wrapper is fantastic, it takes a lot of the ho-hum out of virtualenv, and makes switching and starting projects a snap. My major beef with it is the way it uses entirely different commands to perform it's major functions. Why I need to remember ``lssitepackages`` instead of using ``venvwrapper ls`` is beyond me. A short rant, but that's because venv wrapper is such a fantastic tool.
