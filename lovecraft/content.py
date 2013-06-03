# -*- coding: utf-8 -*-
from datetime import date


class Content(object):
    ''' Generic Content class to be extended by content types
        Expects a jinja2 environment
    '''
    def __init__(self, environment):
        self.environment = environment


class Post(Content):
    """ A simple post object to be invoked from CLI """
    def __init__(self, title="New Post " + str(date.today())):
        self.title = title + " " + str(date.today())
        # this is wonky, find a better way to format it
        self.content = """Title: %s
Category:
Tags:
----
""" % self.title

    def render(self, template):
        ''' returns a jinja2 rendered post'''
        template = self.environment.get_template('post_single.html')
        return template.render(self)


class Page(Content):
    """ """
    def __init__(self, title):
        self.title = title

    def render(self):
        ''' returns a jinja2 rendered post'''
        template = self.environment.get_template('post_single.html')
        return template.render(self)
