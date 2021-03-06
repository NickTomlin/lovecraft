#! /usr/bin/env python
# -*- coding: utf-8 -*-

from lovecraft import site
from lovecraft.content import Post
from lovecraft import util
import argparse
from os import path

# Dev
import inspect


def test(args):
    print("it's working")


def build_site(args):
    site.build_site()


def create_post(args):

    new_post = Post(args.title[0])
    post_path = path.join('source/content/posts', util.get_safe_pathname(new_post.title) + '.md')

    with open(post_path, 'w') as outfile:
        try:
            outfile.write(new_post.content)
        except:
            print('Could not write post')
    print('wrote post "%s" to %s' % (args.title[0], post_path))


if __name__ == '__main__':
    ''' Parse arguements using builtin argparse module.

    1. Clean @todo
    2. Build
    3. Preview @todo
        - how to do this?
            - http mini-server?
        - how to detect file system events?
            - watchdog?
    4. Content types @todo
    5. New Post


    Note: argparse is python 2.7+, so we may want to fallback/switch to another method (getopt, for example)

    Standard arg processing [patterns](http://docs.python.org/2/library/getopt.html#getopt.error).
    For an example, look at David Warings [RTM cli arg parsing](https://bitbucket.org/dwaring87/rtm-cli/src/2a5f697807b4b9f106081352e26e84b6d1e49751/rtm?at=default#cl-4388).
    to throw in the towel, check out [baker](https://pypi.python.org/pypi/Baker/)
    '''

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_post = subparsers.add_parser('post')
    parser_post.add_argument(
        'title',
        default="New Post",
        help="Create a new post, with a title you specify, or a default date hash",
        nargs=1
    )
    parser_post.set_defaults(func=create_post)

    parser_build = subparsers.add_parser('build')
    parser_build.set_defaults(func=build_site)

    parser.test = subparsers.add_parser('test')
    parser.test.set_defaults(func=test)

    # Assign the function specified in .set_default to execute when arg is called
    args = parser.parse_args()
    args.func(args)
