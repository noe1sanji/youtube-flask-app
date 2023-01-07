from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
from pprint import pprint
from app.video_list import get_most_popular_videos

load_dotenv()

service = build("youtube", "v3", developerKey=os.environ["DEVELOPER_KEY"])

results = service.search().list(q="dw documentales", part="id,snippet", maxResults=5).execute()

for row in results.get('items', []):
    pprint(row["snippet"]["title"])
    pprint(row["id"])
    pprint(row)
    print("-"*60)

service.close()

videos = get_most_popular_videos()

for video in videos:
    pprint(row)