#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
#LOAD_CONTENT_CACHE = False

AUTHOR = u'cosmoslx'
AUTHOR_EMAIL = 'cosmoslx@gmail.com'
SITENAME = u'Cosmos of Cosmoslx'
SITESUBTITLE = u'Story about a ordinary boy who want to build a marvelous toy'
SITESUBTITLES = ('A ordinary boy', 'build a marvelous toy')
SITEURL = 'http://blog.cosmoslx.me'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'General'

TIMEZONE = 'Asia/Chongqing'
DEFAULT_DATE = 'fs'
DEFAULT_LANG = u'zh'

SUMMARY_MAX_LENGTH = 20

# Theme
#THEME = 'SoMA2'
#THEME = 'Responsive-Pelican'
THEME = 'bold'
#CSS_FILE = "wide.css"
TYPOGRIFY = True

# PATH
PATH = 'content'
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Plugin
PLUGIN_PATHS = ["/home/cosmoslx/github/pelican-plugins"]
PLUGINS = ["cjk-auto-spacing", "gravatar", "summary", "representative_image",
           "read_more_link",]
SUMMARY_END_MARKER = "<!-- more -->" # keep compatible with octopress

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         )

# Social widget
SOCIAL = (('about me', 'http://about.me/cosmoslx'),
          ('github', 'http://github.com/cosmoslx'),
          )

DEFAULT_PAGINATION = 10
