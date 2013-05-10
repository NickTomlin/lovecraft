#! /usr/bin/env python
# -*- coding: utf-8 -*-

from lovecraft import parse
from lovecraft import post
from os import argv


''' Commands
1. Clean @todo
2. Build @todo
3. Preview @todo
4. Content types @todo
5. New Post @doing
'''


def main(args):
    ''' Parse arguements.
    I'm doing it wrong. I should use one of the standard [patterns](http://docs.python.org/2/library/getopt.html#getopt.error)
    For a resource, look at David Warings [RTM cli arg parsing](https://bitbucket.org/dwaring87/rtm-cli/src/2a5f697807b4b9f106081352e26e84b6d1e49751/rtm?at=default#cl-4388)
    '''
    if args[0] == 'post':
        if args[1]:
            with open(args[1], 'w+') as postfile:
                post = post.Post(title=args[1])
                postfile.write(post.content)
                print ("Created post")
        else:
            print ('No post title specified')

    elif args[0] == 'build':
        parse.create_posts()

    else:
        print('No arguements supplied. Peace out.')


if __name__ == '__main__':
    main(argv[1:])
