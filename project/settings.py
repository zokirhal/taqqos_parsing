import os

# SECRET KEY
SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY')

# DATABASE SETTINGS
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'taqqos_parsing')
DATABASE_USER = os.environ.get('DATABASE_USER', 'taqqos_parsing')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'taqqos_parsing')
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.environ.get('DATABASE_PORT', '5432')
DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
