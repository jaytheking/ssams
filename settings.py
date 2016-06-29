import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
  """Base Config class"""
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  ARTICLES_PER_PAGE = 1
  ARTICLE_BASE_DIR = 'articles/'
  FILE_LIST = os.listdir(ARTICLE_BASE_DIR)
  SECRET_KEY = 'zsbdxjovgnsenbxdjbgvsenvbxdirutouwaerfvbkjsrgjbv'


class ProductionConfig(Config):
  """Configuration for use in production"""
  DEBUG = False


class StagingConfig(Config):
  """Configuration for use in staging"""
  DEVELOPMENT = True
  DEBUG = True


class DevelopmentConfig(Config):
  """Configuration for use in development"""
  DEVELOPMENT = True
  DEBUG = True

class TestingConfig(Config):
  """Configuration for use in production"""
  TESTING = True


dev = DevelopmentConfig()
staging = StagingConfig()
production = ProductionConfig()
