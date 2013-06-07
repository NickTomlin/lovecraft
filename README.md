Lovecraft: a static site generator so terrifyingly simple that it will shred the last remenants of your tattered mortal pysche.

# Structure
source
  - content
    - posts
      - post-title.md
      - post-title2.md
    - pages
      - page1.md
      - page2.md
  - static
    - scss (css / less / stylus ­ handle with plugin?)
    - js
    - img
  - templates
    - base.html
    - single.html (prolly should be "page")
    - single-post.html
    - partials
      - post.html
  - config.yml

# Deps

- Markdown: [Markdown2](https://github.com/trentm/python-markdown2)
- Templating: [Jinja2](http://jinja.pocoo.org/docs/)
- Metadata [pyyaml](https://bitbucket.org/xi/pyyaml)

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

# Science Fiction
- Syntax Highlighting
- Custom content/post types
- Author profile
- Images?
- Social widgets
- Custom Themes directory
- Live preview server
