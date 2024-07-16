import requests
from requests.auth import HTTPBasicAuth
import send_email as send_email
import os
import json
from config import config

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
