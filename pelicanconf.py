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

DIRECT_TEMPLATES = ['tags']
TEMPLATE_PAGES = {}
DELETE_OUTPUT_DIRECTORY = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
THEME_TEMPLATES_OVERRIDES = ['overrides']

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

DELETE_OUTPUT_DIRECTORY = True
DEFAULT_PAGINATION = False
INDEX_SAVE_AS = ''  # NE PAS générer d'index.html automatique pour éviter le conflit

