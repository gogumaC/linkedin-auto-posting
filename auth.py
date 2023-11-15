import configparser as parser
import requests
from requests.auth import HTTPBasicAuth
import send_email
import os

if __name__ == "__main__":
    
    CLIENT_ID=os.getenv("client_id")
    CLIENT_SECRETE=os.getenv("client_secrete")
    REDIRECT_URL=os.getenv("redirect_url")
    CLIENT_EMAIL=os.getenv("client_email")

def get_access_token(auth_code):
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
    print(f"access toekn : {access_token}")
  else :
    print(f"Fail : {response.status_code}, {response.text}")


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
  send_email.send_auth_email(CLIENT_EMAIL,auth_url)
  



