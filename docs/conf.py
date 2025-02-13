import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'OPTIC'
author = 'Noriaki Fukatsu'
release = '1.0'

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']