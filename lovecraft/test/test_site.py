from lovecraft import site
import os
''' Test basic i/o functions
- Reading conent directories
- Recoursing file structure

Lovingly tested with [nose](https://github.com/nose-devs/nose)

@todo create a test config file for variables like post directory, etc.
That way we don't have to change things up everytime the file system
changes.
'''
post = '''
title: Post Title
tags: tips
category: Testing
'''


''' Test Helpers
'''

source_dir = 'test/parse_source'
posts_dir = os.path.join(source_dir, 'posts')


def test_gather_markdown():
    #  use our test directory or it will FREAK out
    result = site.gather_markdown(posts_dir)
    assert len(result) == 3, 'gather did not collect correct number of posts, expected 4, got %s' % len(result)


def test_get_yaml():
    yaml_file = os.path.join(posts_dir, 'yaml.md')
    with open(yaml_file, 'r') as source:
        yaml = site.get_yaml(source.read())

    assert yaml['title'] == 'Title works', 'Yaml did not load correctly'


def test_format_title():
    path = 'test/posts/post1.md'
    title = site.format_title(path)

    assert title == 'post1', 'site.format_title did did not produce expected result, gave: %s got: %s' % (path, title)


def test_format_abnormal_title():
    path = 'test/posts/title\ 2013-05-28.md'
    title = site.format_title(path)
    expected = r'title\ 2013-05-28'

    assert title == expected, 'site.format_title did did not produce expected result, gave: %s expected: %s got: %s' % (path, expected, title)


def test_format_output_path():
    formatted = site.format_output_path('posts', 'post2', '.md')
    expected = 'posts/post2.md'

    assert formatted == expected, 'format_output_path did not properly format path: got %s'

''' Test Site object
'''


def test_sanity():
    new_site = site.Site()
    assert new_site.base_test()


def test_init_defaults():
    new_site = site.Site()
    assert new_site.config_file == 'config.yaml', 'Default option not set'


def test_set_options():
    new_site = site.Site(input_dir=source_dir)
    assert new_site.input_dir == source_dir, 'Provided Custom option not set'


def test_set_and_default():
    new_site = site.Site(input_dir=source_dir)
    assert new_site.input_dir == source_dir and new_site.config_file == 'config.yaml', 'Default and Custom option not properly set'


def test_default_source_path():
    new_site = site.Site()
    assert new_site.posts_source_path == 'source/content/posts', 'Incorrect default source path: %s ' % new_site.posts_source_path



# def test_markdown():
#     '''@todo add a dictionary of markdown here?
#     '''
#     with open('test/posts/post1.md', 'r') as infile:
#         parsed = lovecraft.parse.parse_markdown(infile.read())
#     assert parsed == '<h2>post 1</h2>\n\n<p><em>boo!</em></p>\n', 'Markdown did not parse post1 file correctly'


# def test_format_title():
#     # assert lovecraft.parse.format_title('test/posts/post1.md') == 'post1', 'format_title failed on post1'
#     raw_titles = ['test/posts/post1.md', 'foo.md']
#     expected_titles = ['post1', 'foo']

#     # pythonic [zip](http://stackoverflow.com/a/1919055/1048479)
#     for raw, expected in zip(raw_titles, expected_titles):
#         parsed = lovecraft.parse.format_title(raw)
#         print(parsed)
#         assert parsed == expected, 'got: %s ; expected: %s' % (parsed, expected)


# def test_format_post_url():
#     ''' Is post.href being formatted properly?
#     '''
#     pass


# def test_format_output_path():
#     dir_name = './content/formatted'
#     post_name = 'post1'
#     ext = '.html'
#     expected = './content/formatted/post1.html'
#     joined = lovecraft.parse.format_output_path(dir_name, post_name, ext)
#     assert joined == expected, 'got: %s ; expected: %s' % (joined, expected)


# def test_cp_static():
#     lovecraft.parse.cp_static('static', 'test/parse_results')


# def test_create_posts():
#     ''' @todo this combines a LOT of functionaliy.
#     Split things up to make them more testable?
#     -> move template testing into test/template.py

#     using try methodology from http://stackoverflow.com/a/3770375/1048479
#     '''
#     lovecraft.parse.create_posts('test/source/posts', 'test/parse_results', 'posts')

#     """
#     @todo would it be better to set this up as a tuple of dictionaries? (or keyed tuple?)[http://stackoverflow.com/a/4878962/1048479]
#     from collections import namedtuple
#     >>> Content = namedtuple("content",["expected","parsed"])
#     >>> index = Content(expected='test/parse_expected/index.html', parsed='test/parse_results/index.html')
#     >>> index.expected
#     test/parse_expected/index.html
#     """

#     '''@borked source changes too often to test reliably
#     generated_content = ['test/parse_results/posts/post1.html', 'test/parse_results/index.html']
#     expected_content = ['test/parse_expected/posts/post1.html', 'test/parse_expected/index.html']

#     for generated, expected in zip(generated_content, expected_content):
#         gen_file = open(generated, 'r')
#         expec_file = open(expected, 'r')

#         try:
#             assert gen_file.readlines() == expec_file.readlines(), ('%s does not match %s' % (generated, expected))
#         finally:
#             gen_file.close()
#             expec_file.close()
#     '''
