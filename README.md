[![Build Status](https://travis-ci.org/marcelomoraes28/pyramid-auto-env.svg?branch=master)](https://travis-ci.org/marcelomoraes28/pyramid-auto-env)
[![Coverage Status](https://coveralls.io/repos/github/marcelomoraes28/pyramid-auto-env/badge.svg?branch=auto_env)](https://coveralls.io/github/marcelomoraes28/pyramid-auto-env?branch=auto_env)
[![Pypi Version](https://img.shields.io/badge/pypi-0.0.1-yellow.svg)](https://img.shields.io/badge/pypi-0.0.1-yellow.svg)
[![Python Version](https://img.shields.io/badge/python-2.7%7C3.6-blue.svg)](https://img.shields.io/badge/python-2.7%7C3.6-blue.svg)

# Pyramid auto env
An pyramid library to help a overwrite ini configs with environments.

## Getting Started

These instructions will help you install library and use its features.

### Installing

```
pip install pyramid_auto_env
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
keys = root, myproject

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = INFO
handlers = console

[logger_myproject]
level = DEBUG
handlers =
qualname = myproject

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
export ENV_MAIL_PASSWORD = S3kr3t
```
**CODE**
```python
from pyramid.config import Configurator
from pyramid_auto_env import get_env_or_ini

@get_env_or_ini()
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
