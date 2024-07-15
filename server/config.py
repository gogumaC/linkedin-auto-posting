import os
from dotenv import load_dotenv


class Config:
    _instance=None
    dotenv_path=""
    has_file=False

    def __new__(cls):
        if cls._instance is None:
            cls._instance=super(Config,cls).__new__(cls)
            dir_name=os.path.dirname(os.path.abspath(__file__))
            dir_name=os.path.dirname(dir_name)
            cls.dotenv_path=os.path.join(dir_name,".env")
            
            if not os.path.exists(cls.dotenv_path): 
                #in docker container
                cls.dotenv_path="/run/secrets/.env"
            print(f"env path : {cls.dotenv_path}\n")
            
            if os.path.exists(cls.dotenv_path):
                load_dotenv(cls.dotenv_path)
                cls.has_file=True
        return cls._instance
    
    @staticmethod
    def get(key,default=None):
        return os.getenv(key,default)
    
config=Config()