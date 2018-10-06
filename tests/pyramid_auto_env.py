from tests.conftest import main, main_set_prefix


class TestPyramidAutoEnv:

    def test_without_env(self, payload_env):
        without_env = main(**payload_env)
        assert without_env == payload_env

    def test_with_envs(self, monkeypatch, payload_env):
        monkeypatch.setenv('ENV_MAIL_PASSWORD', 'foo')
        monkeypatch.setenv('ENV_MAIL_USERNAME', 'bar')
        with_env = main(**payload_env)
        payload_env['mail.password'] = 'foo'
        payload_env['mail.username'] = 'bar'
        assert payload_env == with_env

    def test_with_bool_envs(self, payload_env):
        payload_env['mail.password'] = 'True'
        payload_env['mail.username'] = 'FAlSe'
        with_bool = main(**payload_env)
        payload_env['mail.password'] = True
        payload_env['mail.username'] = False
        assert payload_env == with_bool

    def test_with_pyramid_prefix(self, monkeypatch, payload_env):
        monkeypatch.setenv('PYRAMID_MAIL_USERNAME', 'bar')
        with_pyramid_prefix = main_set_prefix(**payload_env)
        payload_env['mail.username'] = 'bar'
        assert payload_env == with_pyramid_prefix
