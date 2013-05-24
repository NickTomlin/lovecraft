# -*- coding: utf-8 -*-
from datetime import date


class Post(object):
    """ A simple post object to be invoked from CLI """
    def __init__(self, title="New Post " + str(date.today())):
        super(Post, self).__init__()
        self.title = title + " " + str(date.today())
        # this is wonky, find a better way to format it
        self.content = """Title: %s
Category:
Tags:
----
        """ % self.title
