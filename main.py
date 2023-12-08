import os
import feedparser
from datetime import datetime, timedelta
import ssl
import sys
from dotenv import load_dotenv
from classes import Posting
import posting

def find_new_posting():

    if hasattr (ssl,'_create_unverified_context') :
        ssl._create_default_https_context=ssl._create_unverified_context

    print(f"\nFinding new posting...from {FEED_URL}\n")

    feed = feedparser.parse(FEED_URL)
    current_time = datetime.now()
    one_hour_ago = current_time - timedelta(hours=1)

    new_postings = []

    if feed.bozo == 1:
        print(f"Error parsing feed: {feed.bozo_exception}\n")
        sys.exit(1)
    
    for index, entry in enumerate(feed['entries']):
    

        published_time = datetime.strptime(entry['published'], "%Y-%m-%dT%H:%M:%S+09:00")

        if published_time > one_hour_ago and published_time <= current_time :
            title = entry['title']
            link = entry['link']
            published_time_str = published_time.strftime("%Y.%m.%d %H:%M")
            new_postings.append({ 'title':title,'link':link,'published_time':published_time_str })
            print(f'#{ index + 1 } : { title } | { published_time_str } | { link } \n ')


    print(f"new posting : {len(new_postings)}")
    return new_postings


if __name__=="__main__":

    local_feed_url=""
    local_request_url=""

    if os.path.isfile('.env'):
        load_dotenv()
        local_feed_url=os.getenv('feed_url')
        local_request_url=os.getenv('request_url')
    
    FEED_URL = os.environ['RSS_FEED_URL'] if os.environ.get('RSS_FEED_URL') != None else local_feed_url
    REQUEST_URL = os.environ['REQUEST_URL'] if os.environ.get('POSTING_CONTENT') != None else local_request_url
    DEFAULT_CONTENT = os.environ['POSTING_CONTENT'] if os.environ.get('POSTING_CONTENT') != None else "New Posting"

    new_postings = find_new_posting()

    for post in new_postings :
        title = post['title']
        link = post['link']
        published_time = post['published_time']
        content = DEFAULT_CONTENT + f"\n[{title}] \npublished : {published_time}"
        posting.post_to_linkedin(Posting(url=link,title=title,content=content))
    