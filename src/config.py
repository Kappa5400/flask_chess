
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    DATABASE = os.path.join(BASE_DIR, 'database.db')
