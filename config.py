import os


class Config(object):
    """Описание всех конфигурационных настроек приложения."""

    # Режим отладки
    DEBUG = True

    # Секретный ключ задается либо в переменной окружения либо непосредственно.
    SECRET_KEY = os.environ.get("SECRET_KEY") or "any_key"

    # Опции подключения к SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://flsk333_user:12345678@localhost/flsk333_db"
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # CSRF настройки, защищают от подмены POST-сообщений
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess"
