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


def get_yaml(text_source):
    ''' (str) -> {'meta_attribute' : 'meta_key', ...}
    Takes a section of YAML and returns a dictionary of keyed metadata

    @borked This function doesn't have much a a purpose now that we've
    removed the .strip('\n---\n')  part from it. Is it redundant?
    '''

    # @borked yaml.load works on plain text so we need a way of testing if
    # if it has actually generated yaml
    parsed_meta = yaml.load(text_source)
    if type(parsed_meta) is not dict:
        print('could not parse meta dict')
        return None
    return parsed_meta


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

    def __init__(self, template_dir='source/templates', input_dir='source', output_dir='build', static_dir='static', config_file='config.yaml'):
        # base paths
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.input_dir = input_dir
        self.posts_dir = 'content/posts'
        self.static_dir = static_dir

        # computed paths
        self.posts_source_path = os.path.join(input_dir, self.posts_dir)
        self.posts_dest_path = os.path.join(output_dir, self.posts_dir)
        self.static_source_path = os.path.join(input_dir, self.static_dir)
        self.static_dest_path = os.path.join(output_dir, self.static_dir)

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

    def ready_build_directory(self):
        ''' Prepare build folder / static files
        1. Clean build directory.
        2. Recreate Build directory.
        3. Create post directory.
        4. Copy Static Files.
        @borked, need to find a way to format options
        '''
        shutil.rmtree(self.output_dir)

        # create build post directory
        os.makedirs(self.output_dir)
        os.makedirs(self.posts_dest_path)

        ''' Copy static files'''

        shutil.copytree(self.static_source_path, self.static_dest_path)

    def gather_content(self):
        ''' Gathers site content, appends a list of post dictionaries to self.formatted_posts
        Given a system path (source_dir):
        1. Look for valid post files with gather_posts (.md)
        2. Grab post 'name' from filename (replace with metadata later on) in post['title]
        3. Convert post content into markdown and store in post['content']
        '''
        # @todo rename this throughout function to just use self.<property>
        posts_output_dir = self.posts_source_path
        posts_gather_path = self.posts_dest_path

        print('Looking for posts in %s' % posts_gather_path)
        posts = gather_posts(posts_gather_path)

        self.formatted_posts = []
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

                formatted_post['meta'] = get_yaml(post_header)
                formatted_post['content'] = markdown2.markdown(markdown_string)

            self.formatted_posts.append(formatted_post)

    def create(self):
        ''' Returns nothing.
        Write gathered posts/pages to build directory
        @todo use post.py's Post()
        '''
        for post in self.formatted_posts:
            # destination is .html
            # ./content/formatted/post1.html
            post_file_path = format_output_path(posts_output_dir, post['filename'], '.html')

            # Write individual posts
            with codecs.open(post_file_path, 'w') as outfile:
                post_template = site.create_post(post)
                outfile.write(post_template)
        print('Wrote %s posts' % len(formatted_posts))
        # write index
        with codecs.open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf8') as indexfile:
            index_template = site.create_index(formatted_posts)
            indexfile.write(index_template)
        # @todo create a 'pages' task
        print('Site Build Complete')


if __name__ == '__main__':
    new_site = Site()
    new_site.gather_content()
    new_site.ready_build_directory()
    new_site.create()
