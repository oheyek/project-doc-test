# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SNWO'
copyright = '2025, Stebnicki i Zelder'
author = 'Stebnicki i Zelder'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

language = 'Polski'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = []

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

extensions.append('breathe')

# Ustawienia Breathe
breathe_projects = {
    "CppProject": "../doxygen_docs/xml"
}
breathe_default_project = "CppProject"
