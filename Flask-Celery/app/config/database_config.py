import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base config"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Development Database Config"""
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"

class ProductionConfig(Config):
    """Production Database Config (change to PostgreSQL or MySQL)"""
    SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost/dbname"


# Store in a dictionary
DatabaseConfig = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
