import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'Thisisyoursecretkey'

class ProductionConfig(Config):
	DEBUG = False

class StagingConfig(Config):
	DEVLOPMENT = True
	TESTING = True

class DevelopmentConfig(Config):
	DEVLOPMENT = True
	DEBUG = True

class TestingConfig(Config):
	TESTING = True

		