# Superset Configuration
import os

# Database settings
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://superset:superset@db/superset'

# Redis for caching and async queries
CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_URL': 'redis://redis:6379/0',
}


# Hive connection string example
HIVE_CONNECTION = {
    'name': 'hive',
    'sqlalchemy_uri': 'hive://hive:password@hiveserver2:10000/dataengineering',
}
# Set the feature flag for enabling SQLLAB
FEATURE_FLAGS = {
    'SQLLAB_BACKEND_PERSISTENCE': True,
}

# Enabling CORS
ENABLE_CORS = True
CORS_OPTIONS = {
    "origins": ["*"],  # Allow all origins
}

# Other configurations
SECRET_KEY = 'ceyceycey'