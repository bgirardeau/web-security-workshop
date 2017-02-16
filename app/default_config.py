# Default Development Configuration
import os
current_directory = os.path.dirname(os.path.abspath(__file__))


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + current_directory + '/test.db'
SECRET_KEY = 'test key'
SESSION_COOKIE_HTTPONLY = False
