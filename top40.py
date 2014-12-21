#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import click
import dotenv
import requests
import requests_cache
import youtube_dl

from apiclient.discovery import build
from apiclient.errors import HttpError

# Read env variables from a .env file if available
dotenv.read_dotenv()

# Cache the API calls and expire after 12 hours
requests_cache.install_cache(expire_after=43200)

TOP40_URL = 'http://ben-major.co.uk/labs/top40/api/singles/'

def _get_charts(url):
    """Retrieves the current UK Top 40 Charts"""
    
    response = requests.get(url).json()
    data = response['entries']

    return data


def _youtube_search(query, max_results=1):
    """Search Youtube for QUERY, returning MAX_RESULTS
        Returns a dict of video ID and TITLE mappings
    """

    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    try:
        DEVELOPER_KEY = os.environ['DEVELOPER_KEY']
    except KeyError as e:
        print "Please set the DEVELOPER_KEY env variable"
        exit()

    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=query,
        part="id,snippet",
        maxResults=max_results
    ).execute()

    # Add each result to a dict, and then display the lists of
    # matching videos

    videos = {
        search_result["snippet"]["title"]: search_result["id"]["videoId"]
        for search_result in search_response.get("items", [])
        if search_result["id"]["kind"] == "youtube#video"}

    # Dict in format {title: id}
    return videos


@click.group()
def top40():
    """A simple command line tool to display songs in the UK Top 40 Charts
    """
    pass


@top40.command()
@click.option(
    '-n', '--num',
    default=10,
    type=click.IntRange(1, 40, clamp=True),
    help='Number of Songs to Display')
def display(num):
    """Displays the top 'num' songs in the chart.
       If 'num' is not provided, it defaults to 10.
    """

    data = _get_charts(TOP40_URL)[:num]

    for index, element in enumerate(data, start=1):
        click.echo(
            '{}. {} - {}'.format(
                index,
                element['title'].encode('utf-8', 'replace'),
                element['artist'].encode('utf-8', 'replace')))


def download(pos):
    """Download the song occupying the position specified"""

    data = _get_charts(TOP40_URL)
    pos -= 1

    search = '{} - {}'.format(
        data[pos]['title'].encode('utf-8', 'replace'),
        data[pos]['artist'].encode('utf-8', 'replace'))
    try:
        dl = _youtube_search(search)
    except HttpError as e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print "Downloading " + dl.keys()[0]
        ydl.download(dl.values())


if __name__ == '__main__':
    top40()
