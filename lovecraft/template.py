from jinja2 import Environment, FileSystemLoader, PackageLoader

# loader = FileSystemLoader('lovecraft/templates')
loader = PackageLoader('lovecraft', 'templates')
env = Environment(loader=loader)


def base_test():
    return False
''' @todo explain post object here
'''


def post(post_obj):
    template = env.get_template('post_single.html')
    return template.render(post=post_obj)


def index(posts_array):
    ''' What gets weird here is that we are passing an [] of posts,
    not a post_obj.
    '''
    template = env.get_template('index.html')
    return template.render(posts=posts_array)
