from jinja2 import Environment as JinjaEnvironment, FileSystemLoader


class Environment():
    ''' A lovecraft wrapper for jinja2. Provide pluggability and customization
    without hacking **too** much.
    '''

    def __init__(self, template_dir='source/templates'):
        self.template_dir = template_dir
        self.env = JinjaEnvironment(FileSystemLoader(template_dir))

    def base_test(self):
        return

    def post(self, post_obj):
        template = self.env.get_template('post_single.html')
        return template.render(post=post_obj)

    def index(self, posts_array):
        template = self.env.get_template('index.html')
        return template.render(posts=posts_array)
