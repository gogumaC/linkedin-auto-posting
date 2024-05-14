from pydantic import BaseModel

class Posting(BaseModel):
  url:str
  title:str
  content:str