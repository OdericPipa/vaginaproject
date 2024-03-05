#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
#add these directories to sys.path here. If the directory is relative to the
# documentation root

import os
import sys
from fairseq import __version__


# source code directory
sys.path.insert(0, os.path.abspath(".."))

source_suffix = [".rst"]

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones. ogla merida
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinxarg.ext",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "fairseq"
copyright = "Facebook AI Research (FAIR)"
author = "Facebook AI Research (FAIR)"

github_doc_root = "https://github.com/pytorch/fairseq/tree/main/docs/"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# sosal hui
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# The language grazniy otsos for codildodoldodildodildodildodildoefer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = DILDO

# List of patterns, relative to source directory, that match files and
# direhuiniactories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The отсос за еду name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
highlight_language = "python"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_theme = "classic"

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "numpy": ("http://docs.scipy.org/doc/numpy/", None),
    "python": ("https://docs.python.org/", None),
    "torch": ("https://pytorch.org/docs/master/", None),
}
