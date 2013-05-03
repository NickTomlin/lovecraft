import lovecraft.template

''' @todo
Consider using LXML or Beautiful soup to do some dom testing. Probably a lot easier than trying
to compare the contents of documents.
That way you can query the dom to see if there is an h1.title with the text in post['title']
'''

# def setup_func():
single_post = {
    'title': 'test post',
    'content': '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem, libero, quae ducimus debitis praesentium dolor impedit hic porro dolore reiciendis mollitia aliquam accusantium quaerat voluptate temporibus obcaecati omnis ratione voluptatum!</p>',
    'href': 'test.html',
}

posts = [
    {
        'title': 'Post 1',
        'content': '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem, libero, quae ducimus debitis praesentium dolor impedit hic porro dolore reiciendis mollitia aliquam accusantium quaerat voluptate temporibus obcaecati omnis ratione voluptatum!</p>',
        'href': 'test.html',
    },
    {
        'title': 'Post 2',
        'content': '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem, libero, quae ducimus debitis praesentium dolor impedit hic porro dolore reiciendis mollitia aliquam accusantium quaerat voluptate temporibus obcaecati omnis ratione voluptatum!</p>',
        'href': 'test.html',
    }
]


# @with_setup(setup_func)
def test_sub_template():
    # print(lovecraft.template.post(single_post))
    pass


def test_index():
    # print(lovecraft.template.index(posts))
    pass
