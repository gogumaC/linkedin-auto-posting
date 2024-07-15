import requests
from requests.auth import HTTPBasicAuth
import os
import dotenv
import json
from config import config

CLIENT_ID=config.get('client_id')
CLIENT_SECRETE=config.get('client_secrete')
REDIRECT_URL=config.get('redirect_url')
CLIENT_EMAIL=config.get('client_email')

async def get_access_token(auth_code):

  print("request access token...\n ")
  token_url="https://www.linkedin.com/oauth/v2/accessToken"
  data={
      'grant_type':'authorization_code',
      'code' : auth_code,
      'redirect_uri':REDIRECT_URL,
      'client_id' : CLIENT_ID,
      'client_secret' : CLIENT_SECRETE
  }

  response=requests.post(token_url,data=data,auth=HTTPBasicAuth(CLIENT_ID,CLIENT_SECRETE))

  if response.status_code==200:
    access_token=response.json().get('access_token')
    
    if config.has_file:
      dotenv.set_key('.env','access_token',access_token)
    else:
      os.environ['access_toekn'] = access_token


    msg=f"Sucessfully get access token! \n please update your access token : \n {access_token}"
    
    print("access token get success!\n")
  else :
    msg=f"Fail : {response.status_code}, {response.text}"
  
  html_msg = msg.replace('\n', '<br>')
  return {"status":response.status_code,"message":html_msg}
  
