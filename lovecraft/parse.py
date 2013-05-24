# -*- coding: utf-8 -*-
import codecs
import os
import glob
import shutil

from jinja2 import Environment as JinjaEnvironment, FileSystemLoader
import markdown2
import yaml
''' dev '''
import inspect


class Site():
    ''' A general purpose class, to contain all of lovecraft's site creation features.
    Provides a touchpoint for Jinja2's environment.
    '''

    def __init__(self, template_dir='source/templates'):
        self.template_dir = template_dir
        self.env = JinjaEnvironment(loader=FileSystemLoader(template_dir))

    def base_test(self, foo):
        return str(foo) + 'wooot'

    def create_post(self, post_obj):
        template = self.env.get_template('post_single.html')
        return template.render(post=post_obj)

    def create_index(self, posts_array):
        template = self.env.get_template('index.html')
        return template.render(posts=posts_array)

    def copy_files(self):
        ''' Make/Clean build folders and copy static files
        '''
        pass


def create_posts(source_dir='source', output_dir='build', posts_output_folder='posts', config='config.yaml', static='static'):
    ''' (str) (str)
    Given a system path (source_dir):
    1. Look for valid post files with gather_posts (.md)
    2. Grab post 'name' from filename (replace with metadata later on) in post['title]
    3. Convert post content into markdown and store in post['content']
    4. Write formatted posts to file at (posts_output_dir)

    @todo this should really be a Class (site), sort of like a Jinja environment.
    most of the functinoality inside can be broken up into smaller methods
    '''
    posts_output_dir = os.path.join(output_dir, posts_output_folder)
    posts_gather_path = os.path.join(source_dir, 'content/posts')

    print('Looking for posts in %s' % posts_gather_path)
    posts = gather_posts(posts_gather_path)

    formatted_posts = []
    ''' @possible Replace with one 'with', using an infile and outfile?
        @todo move this into a seperate function.
    '''
    for post in posts:
        formatted_post = {}
        formatted_post['filename'] = format_title(post)
        formatted_post['href'] = format_output_path(posts_output_folder, formatted_post['filename'], '.html')

        with open(post, 'r') as input_file:
            contents = input_file.read()

            split_content = contents.split('\n---\n')
            post_header = split_content[0]
            post_body = ''.join(split_content[1:])

            formatted_post['meta'] = meta(post_header)
            formatted_post['content'] = parse_markdown(post_body)

        formatted_posts.append(formatted_post)

    ''' Prepare build folder / static files
    1. Clean build directory.
    2. Recreate Build directory.
    3. Create post directory.
    4. Copy Static Files.

    @todo move into Site.ready_build_directory()
    '''
    shutil.rmtree(output_dir)

    # create build post directory
    os.makedirs(output_dir)
    os.makedirs(posts_output_dir)

    ''' Copy static files'''
    static_src = os.path.join(source_dir, static)
    static_dest = os.path.join(output_dir, static)

    shutil.copytree(static_src, static_dest)

    ''' Generate a new jinja Environment '''
    template = Site()

    ''' Write Posts / Index '''
    for post in formatted_posts:
        # destination is .html
        # ./content/formatted/post1.html
        post_file_path = format_output_path(posts_output_dir, post['filename'], '.html')

        # Write individual posts
        with codecs.open(post_file_path, 'w') as outfile:
            post_template = template.create_post(post)
            outfile.write(post_template)
    print('Wrote %s posts' % len(formatted_posts))
    # write index
    with codecs.open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf8') as indexfile:
        index_template = template.create_index(formatted_posts)
        indexfile.write(index_template)
    # @todo create a 'pages' task
    print('Site Build Complete')


def gather_posts(posts_path):
    ''' (str) -> (list) of ['system/path']
    Takes a system path string, and returns a list
    of "valid" non absolute paths to posts
    ['test/posts/post1.md', 'test/posts/post_0.md', 'test/posts/post_2.md', 'test/posts/post_3.md']
    '''
    # this fails if path does not exist from CWD of parse, check for this?
    path = os.path.join(posts_path, '*.md')
    posts = glob.glob(path)  # "pythonic", but possibly unreliable across oses replace with a regex?
    return posts


def meta(post_header):
    ''' (str) -> {'meta_attribute' : 'meta_key', ...}
    Takes a section of YAML and returns a dictionary of keyed metadata

    @borked This function doesn't have much a a purpose now that we've
    removed the .strip('\n---\n')  part from it. Is it redundant?
    '''

    # @borked yaml.load works on plain text so we need a way of testing if
    # if it has actually generated yaml
    parsed_meta = yaml.load(post_header)
    assert type(parsed_meta) == dict, 'meta yaml.load() did not generate a dict'
    return parsed_meta


def parse_markdown(markdown_string):
    ''' (str.md) -> (str.html)
    Given a full text string of markdown, return formatted html.

    '''
    return markdown2.markdown(markdown_string)


def format_title(post_path):
    ''' (str) -> (str)
    Given a string like 'test/posts/post1.md',
    return the post name without the system path
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
    '''
    return os.path.join(dir_name, fname + ext)  # is the '+' concentation too ganky?


def cp_static(src, dest):
    static_dest = os.path.join(dest, src)
    if os.path.exists(static_dest):
        shutil.rmtree(static_dest)
    print('copying from %s to %s' % (src, static_dest))
    shutil.copytree(src, static_dest)


def test():
    ''' Sanity Check. I'm young :|
    '''
    return True
