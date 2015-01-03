#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Basic
AUTHOR = u'cosmoslx'
AUTHOR_EMAIL = 'cosmoslx@gmail.com'
SITENAME = u'Cosmos of Cosmoslx'
SITESUBTITLE = u'Story about a ordinary boy who want to build a marvelous toy'
SITESUBTITLES = ('A ordinary boy', 'build a marvelous toy')
SITEURL = 'http://blog.cosmoslx.me'
RELATIVE_URLS = False

TIMEZONE = 'Asia/Chongqing'
DEFAULT_DATE = 'fs'
DEFAULT_LANG = u'zh'

DELETE_OUTPUT_DIRECTORY = True

SUMMARY_MAX_LENGTH = 20
SUMMARY_END_MARKER = "<!-- more -->" # keep compatible with octopress

# Category
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'General'

# Feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Theme
#THEME = 'SoMA2'
#THEME = 'Responsive-Pelican'
THEME = 'bold'
TYPOGRIFY = True
#CSS_FILE = "wide.css"

# PATH
PATH = 'content'
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Plugin
PLUGIN_PATHS = ["/home/cosmoslx/github/pelican-plugins"]
PLUGINS = ["cjk-auto-spacing", "gravatar", "summary", "representative_image",
           "read_more_link",]

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         )

# Social widget
SOCIAL = (('about me', 'http://about.me/cosmoslx'),
          ('github', 'http://github.com/cosmoslx'),
          )

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
