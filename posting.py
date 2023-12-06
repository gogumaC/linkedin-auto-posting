import requests
import os
import dotenv
from bs4 import BeautifulSoup
import send_email
import auth
import json
from classes import Posting




dotenv.load_dotenv()
ACCESS_TOKEN=os.getenv("access_toekn")

def get_user_urn():
  url='https://api.linkedin.com/v2/userinfo'
  headers={'Authorization': f'Bearer {ACCESS_TOKEN}'}
  response=requests.get(url,headers=headers)

  if response.status_code ==200:
    user_data=response.json()
    user_urn=user_data['sub']
    return user_urn
  else:
    print(f'error : {response.status_code} {response.text}')


def get_og_image(url):
  response=requests.get(url)
  html=response.text

  soup=BeautifulSoup(html,'html.parser')

  og_image=soup.find('meta',property='og:image')
    
  if og_image and og_image.get('content'):
      return og_image['content']
  else:
      return os.getenv("default_og_image")
  
def save_pended_posting(posting:Posting):
  with open('pended.json','w+') as file:
    json.dump(posting.__dict__,file)
  print(f"save pended posting {posting.title}")

def check_already_request():
  return os.stat('pended.json').st_size==0


def post_to_linkedin(posting:Posting):
  print(f"posting {posting.title}...")
  CLIENT_URN=get_user_urn()
  og_image=get_og_image(posting.url)
  url ="https://api.linkedin.com/v2/ugcPosts"
  headers = {
        'LinkedIn-Version': '202210',
        'X-Restli-Proturlocol-Version': '2.0.0',
        "Authorization": f"Bearer {ACCESS_TOKEN}" 
    }

  payload = {
     "author" : f"urn:li:person:{CLIENT_URN}",
     "lifecycleState": "PUBLISHED",
     "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": posting.content
            },
            "shareMediaCategory": "ARTICLE",
            "media": [
                {
                  "status": "READY",
                  "thumbnails": [
                  {
                    "url": og_image
                  }
                  ],
                  "originalUrl": posting.url,
                  "title": {
                      "text": posting.title
                  },
                }
            ]
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }

  }

  response= requests.post(url,headers=headers,json=payload)
  if response.status_code==201:
    print(f"Success posting to linkedin > {posting.title}")
    send_email.send_posing_complete_email(posting_title=posting.title,link=posting.url)
  elif response.status_code==401:
    print(f"need reauth")
    save_pended_posting(posting)
    if check_already_request()==False: 
      auth.start_authorization()
  else :
    print(f"Fail linkedin posting : {response.status_code}, {response.text}")
    send_email.send_posing_fail_email(posting_title=posting.title,code=response.status_code,text=response.text)
