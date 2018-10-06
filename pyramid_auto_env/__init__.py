import os
from pyramid.settings import asbool


def get_env_or_ini(prefix='env'):
    """
    Example with env prefix and kwargs:
        {
            "mail.password": "1234567",
            "mail.username": "marcelomoraes",
            "mail.host": "smtp.pyramid.com"
        }
    environment: ENV_MAIL_PASSWORD=foobar
    :return  {
            "mail.password": "foobar",
            "mail.username": "marcelomoraes",
            "mail.host": "smtp.pyramid.com"
            }

    :param prefix: environment prefix (default: env)
    """
    def func_wrapper(func):
        def wrapper(*args, **kwargs):
            nonlocal prefix
            for k, v in kwargs.items():
                if v.lower() in ['true', 'false']:
                    kwargs[k] = asbool(os.environ.get(prefix.upper() + '_' + k.upper().replace('.', '_'), v))
                else:
                    kwargs[k] = os.environ.get(prefix.upper() + '_' + k.upper().replace('.', '_'), v)
            return func(*args, **kwargs)

        return wrapper

    return func_wrapper
