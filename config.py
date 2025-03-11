
import os
from dotenv import load_dotenv

# Load environment 
load_dotenv()

class Config:
    # Secret key for session management and security
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to save resources