from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from .search import youtube_search
from dateutil import parser
from .video_list import get_most_popular_videos, get_next_popular_videos
import humanize


def get_db():
    conn = sqlite3.connect("app/database.db")
    conn.row_factory = sqlite3.Row
    return conn


LANG = "es_ES"

app = Flask(__name__)


@app.route("/")
def index():
    videos, nextPageToken, prevPageToken = get_most_popular_videos()
    # videos = []

    return render_template(
        "index.html",
        videos=videos,
        nextPageToken=nextPageToken,
        prevPageToken=prevPageToken,
    )


@app.route("/page/<token>", methods=["POST"])
def page(token):
    videos, nextPageToken, prevPageToken = get_next_popular_videos(token)

    return render_template(
        "index.html",
        videos=videos,
        nextPageToken=nextPageToken,
        prevPageToken=prevPageToken,
    )


@app.route("/results/<search>")
def results(search):
    with get_db() as conn:
        results = conn.cursor().execute(
            "select * from search where search_text=?", (search,)
        )

    return render_template("results.html", results=results)


@app.route("/api/results", methods=["POST"])
def api_results():
    search = request.form["search"]
    results = youtube_search(search)

    with get_db() as conn:
        cur = conn.cursor()
        query = """insert into search (
            search_text,
            published_at,
            channel_id,
            title,
            description,
            thumbnails_url,
            channel_title,
            video_id
        ) values (?, ?, ?, ?, ?, ?, ?, ?)"""

        for row in results:
            cur.execute(
                query,
                (
                    search,
                    row["snippet"]["publishedAt"],
                    row["snippet"]["channelId"],
                    row["snippet"]["title"],
                    row["snippet"]["description"],
                    row["snippet"]["thumbnails"]["high"]["url"],
                    row["snippet"]["channelTitle"],
                    row["id"]["videoId"],
                ),
            )

    return redirect(url_for("results", search=search))


@app.template_filter("formatdatetime")
def format_datetime(value, format="%d %b %Y"):
    if value is None:
        return ""

    result = parser.isoparse(value)

    return result.strftime(format)


@app.template_filter("viewsFormat")
def viewsFormat(value):
    if value is None:
        return ""

    if len(value) > 6:
        humanize.i18n.activate(LANG)
        result = humanize.intword(value).replace("millones", "M vistas")
        humanize.i18n.deactivate()
    else:
        result = f"{int(value):,} vistas"

    return result
