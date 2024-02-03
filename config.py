import os
from dotenv import load_dotenv


class Config:
    _instance=None
    dotenv_path=""

    def __new__(cls):
        if cls._instance is None:
            cls._instance=super(Config,cls).__new__(cls)
            dir_name=os.path.dirname(os.path.abspath(__file__))
            cls.dotenv_path=os.path.join(dir_name,".env")
            load_dotenv(cls.dotenv_path)
        return cls._instance
    
    @staticmethod
    def get(key,default=None):
        return os.getenv(key,default)
    
config=Config()