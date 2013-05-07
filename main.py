from lovecraft import parse


def kick_it():
    parse.create_posts('content/posts', 'build')


if __name__ == '__main__':
    kick_it()
