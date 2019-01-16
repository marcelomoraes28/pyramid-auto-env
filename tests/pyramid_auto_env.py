from tests.conftest import main, main_set_prefix
from pyramid_auto_env import replace


class TestPyramidAutoEnv:

    def test_without_env(self, payload_env):
        without_env = main(**payload_env)
        assert without_env == payload_env

    def test_with_envs(self, monkeypatch, payload_env):
        monkeypatch.setenv('AES_MAIL_PASSWORD', 'foo')
        monkeypatch.setenv('AES_MAIL_USERNAME', 'bar')
        monkeypatch.setenv('AES_MAIL_HOST_PORT', '1234')
        with_env = main(**payload_env)
        payload_env['mail.password'] = 'foo'
        payload_env['mail.username'] = 'bar'
        payload_env['mail.host-port'] = '1234'
        assert payload_env == with_env

    def test_with_bool_envs(self, monkeypatch, payload_env):
        monkeypatch.setenv('AES_MAIL_PASSWORD', 'True')
        monkeypatch.setenv('AES_MAIL_USERNAME', 'False')
        with_bool = main(**payload_env)
        payload_env['mail.password'] = True
        payload_env['mail.username'] = False
        assert payload_env == with_bool

    def test_with_pyramid_prefix(self, monkeypatch, payload_env):
        monkeypatch.setenv('PYRAMID_MAIL_USERNAME', 'bar')
        with_pyramid_prefix = main_set_prefix(**payload_env)
        payload_env['mail.username'] = 'bar'
        assert payload_env == with_pyramid_prefix


class TestReplace:
    def test_replace_with_prefix(self, monkeypatch, payload_env):
        monkeypatch.setenv('PYRAMID_MAIL_USERNAME', 'bar')
        monkeypatch.setenv('PYRAMID_MAIL_HOST', 'foo')
        monkeypatch.setenv('PYRAMID_MAIL_PASSWORD', 'foo-bar')
        with_pyramid_prefix = replace('PYRAMID', **payload_env)
        payload_env['mail.username'] = 'bar'
        assert 'bar' == with_pyramid_prefix['mail.username']
        assert 'foo' == with_pyramid_prefix['mail.host']
        assert 'foo-bar' == with_pyramid_prefix['mail.password']
