import requests
import os
import dotenv

class Posting():
  url:str
  title:str
  content:str

dotenv.load_dotenv()
ACCESS_TOKEN=os.getenv("access_toekn")

def post_to_linkedin(posting:Posting):
  CLIENT_URN=os.getenv("client_secrete")
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


