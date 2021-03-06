from common.config import SharedBaseConfig, SharedDevConfig, SharedTestConfig, SharedProdConfig
import os

class BaseConfig(SharedBaseConfig):

    REDIS_URL = os.environ.get('REDIS_URL', 'redis://')
    CORS_SUPPORTS_CREDENTIALS = True
    ALLOWED_ORIGINS = ['http://www.pwnedhub.com:5000', 'http://test.pwnedhub.com:5001']
    INBOX_PATH = os.environ.get('INBOX_PATH', '/tmp/inbox')

class Development(SharedDevConfig, BaseConfig):

    pass

class Test(SharedTestConfig, BaseConfig):

    pass

class Production(SharedProdConfig, BaseConfig):

    ALLOWED_ORIGINS = ['http://www.pwnedhub.com', 'http://test.pwnedhub.com']
