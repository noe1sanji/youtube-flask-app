from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from .search import youtube_search, next_youtube_search
from .video_list import get_most_popular_videos, get_next_popular_videos
import humanize
import arrow


LANG = "es_ES"

app = Flask(__name__)


@app.route("/")
def index():
    videos, nextPageToken, prevPageToken = get_most_popular_videos()

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


@app.route("/results/<search>", methods=["GET"])
def results(search):
    videos, nextPageToken, prevPageToken = youtube_search(search)

    return render_template(
        "results.html",
        videos=videos,
        searchNextPageToken=nextPageToken,
        searchPrevPageToken=prevPageToken,
        searchText=search,
    )


@app.route("/results", methods=["POST"])
def form_search_results():
    search = request.form["search"]

    return redirect(
        url_for(
            "results",
            search=search,
        )
    )


@app.route("/results/<search>/<token>", methods=["POST"])
def next_results(search, token):
    videos, nextPageToken, prevPageToken = next_youtube_search(search, token)

    return render_template(
        "results.html",
        videos=videos,
        searchNextPageToken=nextPageToken,
        searchPrevPageToken=prevPageToken,
        searchText=search,
    )


@app.template_filter("formatDatetime")
def format_datetime(value):
    if value is None:
        return ""

    result = arrow.get(value).humanize(locale=LANG)

    return result


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
