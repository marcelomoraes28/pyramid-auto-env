[![Build Status](https://travis-ci.org/marcelomoraes28/pyramid-auto-env.svg?branch=master)](https://travis-ci.org/marcelomoraes28/pyramid-auto-env)
[![Coverage Status](https://coveralls.io/repos/github/marcelomoraes28/pyramid-auto-env/badge.svg?branch=auto_env)](https://coveralls.io/github/marcelomoraes28/pyramid-auto-env?branch=auto_env)
[![Pypi Version](https://img.shields.io/badge/pypi-0.1.2-yellow.svg)](https://img.shields.io/badge/pypi-0.0.1--alpha-yellow.svg)
[![Python Version](https://img.shields.io/badge/python-2.7%7C3.6-blue.svg)](https://img.shields.io/badge/python-2.7%7C3.6-blue.svg)

# Pyramid auto env
A pyramid library to help overwrite ini configs with environment variables.

## Getting Started

These instructions will help you install library and use its features.

### Installing

```
pip install pyramid-auto-env
```

## Running the tests
Install test dependencies
```
pip install -e ".[test]"
```

Run test
```
pytest
```

## Using

Replacing the mail.password of the inifile with environment variable

**INI FILE**
```
###
# app configuration
# https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/environment.html
###

[app:main]
use = egg:myproject

pyramid.reload_templates = true
pyramid.debug_authorization = false
pyramid.debug_notfound = false
pyramid.debug_routematch = false
pyramid.default_locale_name = en
pyramid.includes =
    pyramid_debugtoolbar

mail.password = local

# By default, the toolbar only appears for clients from IP addresses
# '127.0.0.1' and '::1'.
# debugtoolbar.hosts = 127.0.0.1 ::1

###
# wsgi server configuration
###

[server:main]
use = egg:waitress#main
listen = localhost:6543

###
# logging configuration
# https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/logging.html
###

[loggers]
keys = root, pyramid_auto_env

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = INFO
handlers = console

[logger_pyramid_auto_env]
level = INFO
handlers = console
qualname = pyramid_auto_env
propagate = 0

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(asctime)s %(levelname)-5.5s [%(name)s:%(lineno)s][%(threadName)s] %(message)s

```

**ENVIRONMENT**
```
export MYPROJ_MAIL_PASSWORD = S3kr3t
```
**CODE**
```python
from pyramid.config import Configurator
from pyramid_auto_env import get_env_or_ini

@autoenv_settings(prefix='myproj')
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()

```

## ENVVAR Format

The environment variable lookup will search for `<prefix.upper()>_<settings_name.upper().replace(['.-', '_'])>`

### Examples (prefix=MYPROJ):
```
host.url -> MYPROJ_HOST_URL
mail-smtp -> MYPROJ_MAIL_SMTP
my.project.super-secret -> MYPROJ_MY_PROJECT_SUPER_SECRET
```
