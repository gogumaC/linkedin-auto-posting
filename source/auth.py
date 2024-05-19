import requests
from requests.auth import HTTPBasicAuth
import send_email as send_email
import os
import dotenv
import json
from classes import Posting
import posting as posting
from config import config

dotenv.load_dotenv()
CLIENT_ID=config.get('client_id')
CLIENT_SECRETE=config.get('client_secrete')
REDIRECT_URL=config.get('redirect_url')
CLIENT_EMAIL=config.get('client_email')

def start_authorization():
  print("authorization start...\n")
  AUTH_URL="https://www.linkedin.com/oauth/v2/authorization"

  auth_params={
      'response_type':'code',
      'client_id':CLIENT_ID,
      'redirect_uri':REDIRECT_URL,
      'scope':'openid%20profile%20email%20w_member_social'
  }

  auth_url = f"{AUTH_URL}?{'&'.join([f'{k}={v}' for k , v in auth_params.items()])}"

  print("please check your email for reauthorization.\n\n")
  send_email.send_auth_email(auth_url)


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
    
    dotenv.set_key('.env','access_token',access_token)
    msg="Sucessfully get access token!"
    print(msg)
    if(posting.check_pended_posting_empty()==False):
      with open('pended.json','r+') as file:
        data=json.load(file)
        pended_posting=Posting(**data)
        posting.post_to_linkedin(pended_posting)
        file.seek(0)
        file.truncate()
  else :
    msg=f"Fail : {response.status_code}, {response.text}"
  
  return {"status":response.status_code,"message":msg}
  

if __name__ == "__main__" :
  start_authorization()