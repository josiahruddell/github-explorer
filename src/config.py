class Config(object):
    DEBUG = True
    GITHUB_API_URL = 'https://api.github.com'

class LocalConfig(Config):
    pass


# current is a module level variable
# for accessing configuration object
current = LocalConfig


def init(app):
    # set application config in flask
    app.config.from_object(LocalConfig)