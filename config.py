import os
basedir = os.path.abspath(os.path.dirname(__file__))

class config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'need-to-change'

class ProductionConfig(config):
	DEBUG = False

class StagingConfig(config):
	DEVELOPMENT = True
	DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True