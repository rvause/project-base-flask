DEBUG = True
SECRET_KEY = 'changeme'
STATIC = '/static/'


try:
    from local_config import *
except ImportError:
    print 'local_config not imported'
