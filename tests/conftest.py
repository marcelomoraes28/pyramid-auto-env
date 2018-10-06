from pytest import fixture
from pyramid_auto_env import autoenv_settings


@fixture(scope="function")
def payload_env():
    return {"mail.password": "1234567",
            "mail.username": "marcelomoraes",
            "mail.host": "smtp.pyramid.com",
            "mail.host-port": '9876'}


@autoenv_settings()
def main(*args, **kwargs):
    return kwargs

@autoenv_settings(prefix='pyramid')
def main_set_prefix(*args, **kwargs):
    return kwargs
