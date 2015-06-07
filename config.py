# _*_ coding: utf-8 _*_
# ...
# available laguages

LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

CSRF_ENABLED = True
SECRET_KEY = "hahaha"

OPENID_PROVIDERS = [
{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
{'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
{'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
{'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

#### SQLite config####
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#### Mail server setting ####
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_USERNAME = 'username'
MAIL_PASSWORD = 'password'

ADMINS = ['abc@def.com']

#### Pagination ####
POSTS_PER_PAGE = 3

#### Search ####
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

#### Microsoft Translation ####
MS_TRANSLATOR_CLIENT_ID = 'xxx'
MS_TRANSLATOR_CLIENT_SECRET = 'xxx'
