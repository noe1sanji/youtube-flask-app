from dotenv import load_dotenv
import os
from googleapiclient.discovery import build


def get_most_popular_videos():
    load_dotenv()

    service = build("youtube", "v3", developerKey=os.environ["DEVELOPER_KEY"])

    results = (
        service.videos()
        .list(
            part="id,snippet,contentDetails,player,statistics",
            chart="mostPopular",
            maxResults=25,
            regionCode="mx",
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

    data = [row for row in results.get("items", [])]

    service.close()

    return data, nextPageToken, prevPageToken


def get_next_popular_videos(page_token):
    load_dotenv()

    service = build("youtube", "v3", developerKey=os.environ["DEVELOPER_KEY"])

    results = (
        service.videos()
        .list(
            part="id,snippet,contentDetails,player,statistics",
            chart="mostPopular",
            maxResults=25,
            regionCode="mx",
            pageToken=page_token,
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

    data = [row for row in results.get("items", [])]

    service.close()

    return data, nextPageToken, prevPageToken
