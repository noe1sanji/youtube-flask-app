from dotenv import load_dotenv
import os
from googleapiclient.discovery import build


def youtube_search(text):
    load_dotenv()

    service = build("youtube", "v3", developerKey=os.environ["DEVELOPER_KEY"])

    results = (
        service.search()
        .list(q=text, part="id,snippet", maxResults=25, type="video")
        .execute()
    )

    try:
        nextPageToken = results["nextPageToken"]
    except KeyError:
        nextPageToken = None

    try:
        prevPageToken = results["prevPageToken"]
    except KeyError:
        prevPageToken = None

    videos = [row for row in results.get("items", [])]

    service.close()

    return videos, nextPageToken, prevPageToken


def next_youtube_search(searchText, pageToken):
    load_dotenv()

    service = build("youtube", "v3", developerKey=os.environ["DEVELOPER_KEY"])

    results = (
        service.search()
        .list(
            q=searchText,
            part="id,snippet",
            maxResults=25,
            type="video",
            pageToken=pageToken,
        )
        .execute()
    )

    try:
        nextPageToken = results["nextPageToken"]
    except KeyError:
        nextPageToken = None

    try:
        prevPageToken = results["prevPageToken"]
    except KeyError:
        prevPageToken = None

    videos = [row for row in results.get("items", [])]

    service.close()

    return videos, nextPageToken, prevPageToken
