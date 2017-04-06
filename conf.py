# -*- coding: utf-8 -*-
#
# Carbon documentation build configuration file, created by
# sphinx-quickstart on Fri Feb  5 17:12:58 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# Import Carbon Sphinx theme from common
sys.path.insert(0, os.path.abspath(
    os.path.dirname(os.path.realpath(__file__)),
))
import carbon_theme

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = [carbon_theme.get_html_templates_path()]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Carbon'
copyright = u'2017, ObjectLabs Corporation'
author = u'Carbon'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.1.0'
# The full version, including alpha/beta/rc tags.
release = u'0.1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

primary_domain = 'js'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'carbon_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 3,
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [carbon_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Carbondoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Carbon.tex', u'Carbon Documentation',
     u'Chris Chang, Will Shulman', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'carbon', u'Carbon Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Carbon', u'Carbon Documentation',
     author, 'Carbon', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
#epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True

intersphinx_mapping = {
    'sphinx': ('http://www.sphinx-doc.org/en/stable/', None),
}

on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    environment = 'prod'
else:
    environment = 'dev'

html_context = {
    'local_rtd_menu': True,
}


def patch_object_description(app):
    from sphinx.domains.javascript import JSXRefRole
    from sphinx.directives import ObjectDescription
    from sphinx import addnodes
    from docutils.parsers.rst import directives
    from docutils import nodes

    # Patch Javascript domain to remove parens on class refs
    app.domains['js'].roles['class'] = JSXRefRole()

    # Add hidden flag to object options
    ObjectDescription.option_spec['hidden'] = directives.flag
    ObjectDescription.option_spec['heading'] = directives.flag
    ObjectDescription.option_spec['use_long_name'] = directives.flag

    # Patch the run method to remove desc_signature nodes if the hidden flag is
    # specified
    wrapped_run = ObjectDescription.run

    def patched_run(self):
        """Patch the ObjectDescription run method to override return nodes

        This allows for use of the two added options:

        hidden
            Hide the node from output, don't add a linkable node to the output.
            This is useful for breaking up a class definition with headings. You
            should define one similar class without this option, or with the
            ``heading`` option below. This should normally be used with
            ``noindex`` as well

        heading
            Hide the node from output, but give a linkable element in the
            output. If you'd rather use headings in place of the domain
            directive nodes, use this in combination with a heading.

        use_long_name
            Because the Javascript linking across objects is currently broken by
            not respecting object nesting correctly, full names should be used
            to define objects and link. Extraneous prefixing is removed by
            default, this option enables showing the full namespace prefix.
        """
        (index, node) = wrapped_run(self)
        if 'hidden' in self.options:
            for (n, child) in enumerate(node):
                if isinstance(child, addnodes.desc_signature):
                    del node[n]

        if 'heading' in self.options:
            elem = nodes.section()
            for (n, child) in enumerate(node):
                if isinstance(child, addnodes.desc_signature):
                    elem = nodes.container()
                    elem['ids'] = child['ids']
                    elem['names'] = child['names']
                    node[n] = elem

        if 'use_long_name' not in self.options:
            for (_, child) in enumerate(node):
                if isinstance(child, addnodes.desc_signature):
                    for (n, sig_child) in enumerate(child):
                        if isinstance(sig_child, addnodes.desc_addname):
                            del child[n]

        return [index, node]

    ObjectDescription.run = patched_run


def remove_listener(app):
    # Remove html-page-context override installed by readthedocs_ext
    try:
        from readthedocs_ext.readthedocs import update_body
        for (key, fn) in app._listeners['html-page-context'].items():
            if fn is update_body:
                app.disconnect(key)
        app.add_javascript('readthedocs-data.js')
        app.add_javascript('readthedocs-dynamic-include.js')
    except ImportError:
        pass


def setup(app):
    app.connect('builder-inited', patch_object_description)
    app.connect('builder-inited', remove_listener)
    app.add_stylesheet('style.css')
    app.add_javascript('carbon.js')
    app.add_config_value('environment', '', 'env')
