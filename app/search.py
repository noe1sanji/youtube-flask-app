from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
from pprint import pprint


def youtube_search(text):
    load_dotenv()

    service = build("youtube", "v3", developerKey=os.environ["DEVELOPER_KEY"])

    results = service.search().list(q=text, part="id,snippet", maxResults=5, type="video").execute()

    data = [row for row in results.get('items', [])]

    service.close()

    return data