Lovecraft: a static site generator so horrifyingly simple that it will shred the last remenants of your tattered mortal pysche.

> current status: a hacky, labour of love. Use at your own peril. Python
> 2.7 only at the moment.

# Usage

1. Clone this repository: ``git clone  https://github.com/NickTomlin/lovecraft my_blog``.
2. ``cd`` into ``my_blog``
2. Use ``python main.py post`` to create posts (you could do it by hand, but why
   bother?)
3. Build a site with ``python main.py build`` 

```
# Create a new post.md file (in source directory)
python main.py post "My sweet post"
>>> wrote post "my sweet post" to
>>> source/content/posts/my_sweet_post_2013-06-10.md
# Build site
python main.py build
>>> wrote 3 posts
>>> site build complete
```

# Structure
source
  - content
    - posts
      - post-title.md
      - post-title2.md
    - (pages -- v1)
  - static
    - css (automatically generated -- v1)
    - js
    - img
  - templates
    - base.html
    - single.html
    - single-post.html
    - partials
      - post.html
  - config.yml

# Deps

- Markdown: [Markdown2](https://github.com/trentm/python-markdown2)
- Templating: [Jinja2](http://jinja.pocoo.org/docs/)
- Metadata: [pyyaml](https://bitbucket.org/xi/pyyaml)
- Testing: [nose](https://nose.readthedocs.org/en/latest/)

# Inspiration

- Google IO 2012 slides
- Cactus
- Octopress

# Issues
- Seperating Content / Theme / Logic
-- There doesn't seem to be a good approach for this :(
-- Maybe just start out by using a seperate "theme" folder
- Posts
-- Do they have their own folder?
--- It'd be nice to handle both (ala, pelican)
--- But... having one file is more portable

# Current Features

## V 0.0
- Converts posts to markdown
-- Including metadata
- Links static CSS/JS
- Some sort of test coverage
- Command line utility

# Roadmap

## V 0.1
- Assembles posts into archive page
- compress / minify static assets?
- better checks for URL safe post href's
- CLI

## V 0.2 
- Create a proper Package

# Science Fiction
- Syntax Highlighting
- Custom content/post types
- Author profile
- Images?
- Social widgets
- Custom Themes directory
- Live preview server
