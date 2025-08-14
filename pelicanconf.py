AUTHOR = 'Pierre Briaud'
SITENAME = 'Pierre Briaud'
SITEURL = ""

THEME = 'pelican-themes/notmyidea-cms'
PATH = "content"

STATIC_PATHS = ['static']

EXTRA_PATH_METADATA = {
    'static/custom.css': {'path': 'custom.css'},
}

TIMEZONE = 'Europe/Oslo'
DEFAULT_LANG = 'en'

PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

DIRECT_TEMPLATES = ['tags', 'categories']
TEMPLATE_PAGES = {}
DELETE_OUTPUT_DIRECTORY = True

DISPLAY_PAGES_ON_MENU = True

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

DELETE_OUTPUT_DIRECTORY = True
DEFAULT_PAGINATION = False
SITEURL = 'https://pierrebriaud.github.io'

INDEX_SAVE_AS = ''  # NE PAS générer d'index.html automatique pour éviter le conflit

