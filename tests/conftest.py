from pytest import fixture
from pyramid_auto_env import get_env_or_ini


@fixture(scope="function")
def payload_env():
    return {"mail.password": "1234567",
            "mail.username": "marcelomoraes",
            "mail.host": "smtp.pyramid.com"}

@get_env_or_ini()
def main(*args, **kwargs):
    return kwargs

@get_env_or_ini(prefix='pyramid')
def main_set_prefix(*args, **kwargs):
    return kwargs

