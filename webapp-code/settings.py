import os
from libs import oauth

DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Devel')

def get_host():
  return "http://" + os.environ['SERVER_NAME'] + ((':' + os.environ['SERVER_PORT']) if os.environ['SERVER_PORT'] != '80' else '')

SECURE_COOKIE = 'b923db28-0eb8-45fe-93c7-874dac458079'

OAUTH_CALLBACK_URL = '%s/%s' % (get_host(), 'oauth/verify')