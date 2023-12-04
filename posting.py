import requests
import os
import dotenv
from pydantic import BaseModel

class Posting(BaseModel):
  url:str
  title:str
  content:str

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

def post_to_linkedin(posting:Posting):
  CLIENT_URN=get_user_urn()
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
                    "url": "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg"
                  }
            ],
                    "originalUrl": posting.url
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
    print("Success linkedin posting")
  else :
    print(f"Fail linkedin posting : {response.status_code}, {response.text}")


if __name__ == "__main__":
  post_to_linkedin(Posting(url="https://gogumac.github.io/", title="testdsdfds", content="testing auto post!"))

