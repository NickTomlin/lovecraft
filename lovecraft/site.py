# -*- coding: utf-8 -*-
import codecs
import os
import glob
import shutil
import datetime

from jinja2 import Environment as JinjaEnvironment, FileSystemLoader
import markdown2
import yaml
''' dev '''
import inspect


def build_site():
    ''' Wraps all the functionality of Site
    into a single call. Is ugly. Baugh.
    '''
    new_site = Site()
    new_site.gather_content()
    new_site.ready_build_directory()
    new_site.create()


def split_yaml_and_content(raw_text):

    ''' (str) -> {'meta_attribute' : 'meta_key', ...}, (str)
    Given a document with a yaml header (signified by '---'):

    1. Strip off the header information before '---'
    2. Grab the rest of the document afterwards
    3. Process the first one as YAML

    Return the processed yaml, and the unformatted "body"

    '''

    split = raw_text.split('\n---\n')
    header = split[0]
    body = split[0:]

    # @borked yaml.load works on plain text so we need a way of testing if
    # if it has actually generated yaml
    parsed_yaml = get_yaml(header)

    return parsed_yaml, body


def get_yaml(text_source):
    ''' (str) -> {'meta_attribute' : 'meta_key', ...}
    Takes a section of YAML and returns a dictionary of keyed metadata

    @borked This function doesn't have much a a purpose now that we've
    removed the .strip('\n---\n')  part from it. Is it redundant?
    @todo make this more hookable, in order to use differnt meta?
    '''
    # @borked yaml.load works on plain text so we need a way of testing if
    # if it has actually generated yaml
    parsed_meta = yaml.load(text_source)
    if type(parsed_meta) is not dict:
        print('could not parse meta dict')
        return None
    return parsed_meta


def gather_markdown(markdown_path):
    ''' (str) -> (list) of ['system/path']
    Takes a system path string, and returns a list
    of "valid" non absolute paths to posts
    ['test/posts/post1.md', 'test/posts/post_0.md', 'test/posts/post_2.md', 'test/posts/post_3.md']
    '''
    # this fails if path does not exist from CWD of parse, check for this?
    path = os.path.join(markdown_path, '*.md')
    posts = glob.glob(path)  # "pythonic", but possibly unreliable across oses replace with a regex?
    return posts


def format_title(post_path):
    ''' (str) -> (str)
    Given a string like 'test/posts/post1.md',
    return the post name without the system path for printing in HTML
    '''
    # split on '/' (hopefully this is okay with windows paths?)
    # since the file name is at the end of a path, we just grab that
    name_with_ext = post_path.split('/')[-1]
    ext_index = name_with_ext.find('.')

    return name_with_ext[:ext_index]


def format_output_path(dir_name, fname, ext):
    '''(str) (str) (str) -> (str)
    joins dir_name, fname, ext
    and returns a full system path.

    @todo is this even necessary?
    @todo normalize path names?
    '''
    return os.path.join(dir_name, fname + ext)  # is the '+' concentation too ganky?


def test():
    ''' Sanity Check. I'm young :|
    '''
    return True


class Site():
    ''' Holds all meta info, and core functionality for a lovecraft site.

    Also provides a touchpoint for Jinja2's environment in the site.env property
    '''

    def __init__(self, input_dir='source', template_dir='templates', output_dir='build', static_dir='static', config_file='config.yaml'):
        # base paths
        self.output_dir = output_dir
        self.input_dir = input_dir
        self.posts_dir = 'content/posts'
        self.static_dir = static_dir

        # joined paths
        self.template_dir = os.path.join(self.input_dir, template_dir)  # source/templates
        self.posts_source_path = os.path.join(self.input_dir, self.posts_dir)  # source/content/posts
        self.posts_dest_dir = os.path.join(self.output_dir, self.posts_dir)  # build/content/posts
        self.static_source_path = os.path.join(self.input_dir, self.static_dir)  # source/static
        self.static_dest_path = os.path.join(self.output_dir, self.static_dir)  # build/static

        # meta
        self.config_file = config_file

        '''@future '''
        # self.gather_meta()

    def base_test(self):
        ''' Sanity Check
        '''
        return True

    def gather_meta(self):
        ''' Parse yaml document
        '''
        with open(self.config_file, 'r') as infile:
            meta = get_yaml(infile.read())
            if meta is not None:
                self.meta = meta
            else:
                print('site could not parse meta ')

    # @todo convert this into a function that just taks a generic tmpl name?
    def create_post(self, post_obj):
        template = self.env.get_template('post_single.html')
        return template.render(post=post_obj)

    def create_index(self, posts_array):
        template = self.env.get_template('index.html')
        return template.render(posts=posts_array)

    def sort_posts(self):
        def sort_with_none(post):
            if 'date' in post:
                return datetime.datetime.strptime(post['date'], '%Y-%m-%d')

            # if not, just send the post to the "bottom"
            return datetime.datetime(1978, 1, 1)

        self.posts.sort(key=sort_with_none, reverse=True)

    def ready_build_directory(self):
        ''' Prepare build folder / static files
        1. Remove build directory
        2. Recreate Build directory.
        3. Create post directory.
        4. Copy Static Files.
        '''
        shutil.rmtree(self.output_dir)

        # create build post directory
        os.makedirs(self.output_dir)
        os.makedirs(self.posts_dest_dir)

        ''' Copy static files'''

        shutil.copytree(self.static_source_path, self.static_dest_path)

    def gather_content(self):
        ''' gathers site content, appends a list of post dictionaries to self.posts
        given a system path (source_dir):
        1. look for valid post files with gather_markdown (.md)
        2. grab post 'name' from filename (replace with metadata later on) in post['title]
        3. convert post content into markdown and store in post['content']
        '''
        raw_post_files = gather_markdown(self.posts_source_path)

        formatted_posts = []

        for raw_post in raw_post_files:
            formatted_post = {}
            formatted_post['filename'] = format_title(raw_post)
            formatted_post['href'] = format_output_path(self.posts_dir, formatted_post['filename'], '.html')  # build/content/posts/post.html

            with open(raw_post, 'r') as input_file:
                contents = input_file.read()

                split_content = contents.split('\n---\n')
                post_header = split_content[0]
                post_body = ''.join(split_content[1:])

                formatted_post['meta'] = get_yaml(post_header)
                formatted_post['content'] = markdown2.markdown(post_body)
                formatted_posts.append(formatted_post)

        self.posts = formatted_posts

    def create(self):
        ''' Returns nothing.
        Write gathered posts/pages to build directory
        @todo use post.py's Post()
        '''

        self.env = JinjaEnvironment(loader=FileSystemLoader(self.template_dir))
        self.sort_posts()  # sorts in place

        for post in self.posts:
            # destination is .html
            # ./content/formatted/post1.html
            post_file_dir = format_output_path(self.posts_dest_dir, post['filename'], '.html')  # content/posts

            with codecs.open(post_file_dir, 'w') as outfile:
                outfile.write(self.create_post(post))

        print('Wrote %s posts' % len(self.posts))

        with codecs.open(os.path.join(self.output_dir, 'index.html'), 'w', encoding='utf8') as indexfile:
            indexfile.write(self.create_index(self.posts))
        # @todo create a 'pages' task
        print('Site Build Complete')
