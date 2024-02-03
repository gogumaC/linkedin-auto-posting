import os
from dotenv import load_dotenv

class Config:
    _instance=None

    def __new__(cls):
        if cls._instance is None:
            cls._instance=super(Config,cls).__new__(cls)
            dotenv_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),".env")
            load_dotenv(dotenv_path)
        return cls._instance
    
    @staticmethod
    def get(key,default=None):
        return os.getenv(key,default)