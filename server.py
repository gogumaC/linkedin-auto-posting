from fastapi import FastAPI
import configparser as parser
import requests
from requests.auth import HTTPBasicAuth
import auth

app=FastAPI()

@app.get("/api")
async def root():
    return {"message":"yubin server"}

@app.get("/linkedin")
async def renew_access_token(code:str):
    res= await auth.get_access_token(code)
    return res


if __name__ == "__main__":
    properties=parser.ConfigParser()
    properties.read('./config.ini')
    url_config=properties['URL']
    client_config=properties['CLIENT']
    CLIENT_ID=client_config['client_id']
    CLIENT_SECRETE=client_config['client_secrete']
    REDIRECT_URL=url_config['redirect_url']
    
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)


