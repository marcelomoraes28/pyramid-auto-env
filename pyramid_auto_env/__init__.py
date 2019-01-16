import logging
import os
from functools import wraps

from pyramid.settings import asbool


logger = logging.getLogger(__name__)


def replace(prefix, *args, **kwargs):
    """
    Example:
          from pyramid_auto_env import replace
          settings = get_appsettings('development.ini')
          update_settings = replace('AES', **settings)
    """
    for k, v in kwargs.items():
        transformed_key = "{}_{}".format(prefix.upper(), k.upper().replace('.', '_').replace('-', '_'))
        envvar_value = os.environ.get(transformed_key)
        if not envvar_value:
            continue
        kwargs[k] = asbool(envvar_value) if envvar_value.lower() in ['true', 'false'] else envvar_value
        logger.info('Found settings replacement for "{}" at "{}". Setting it up.'.format(k, transformed_key))
    return kwargs


def autoenv_settings(prefix='AES'):
    """
    Example with aes prefix and kwargs:
        {
            "mail.password": "1234567",
            "mail.username": "marcelomoraes",
            "mail.host": "smtp.pyramid.com"
        }
    environment: AES_MAIL_PASSWORD=foobar
    :return  {
            "mail.password": "foobar",
            "mail.username": "marcelomoraes",
            "mail.host": "smtp.pyramid.com"
            }

    :param prefix: environment prefix (default: AES)
    """
    def func_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            replace_envs = replace(prefix, *args,**kwargs)
            return func(*args, **replace_envs)

        return wrapper

    return func_wrapper
