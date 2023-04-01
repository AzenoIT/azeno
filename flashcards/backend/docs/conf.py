# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Django settings ---------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#django-settings
import os
import sys

import django

from datetime import datetime
from importlib.machinery import SourceFileLoader


sys.path.insert(0, os.path.abspath(".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

author = "Azeno Team"
project = "flashcards"

year = datetime.now().year
if year > 2023:
    copyright = f"2023-{year}, {author}"
else:
    copyright = f"2023, {author}"


mode = SourceFileLoader("config", "../config/__init__.py").load_module()
release = mode.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "renku"
html_static_path = ["_static"]
html_logo = "_static/azeno_logo.png"
