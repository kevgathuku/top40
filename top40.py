#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import click
import requests
import requests_cache
import youtube_dl

from apiclient.discovery import build
from apiclient.errors import HttpError

DEVELOPER_KEY = os.environ['DEVELOPER_KEY']
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Cache the API calls and expire after 12 hours
requests_cache.install_cache(expire_after=43200)

def get_charts():
    """Retrieves the current UK Top 40 Charts"""

    url = 'http://ben-major.co.uk/labs/top40/api/singles/'
    response = requests.get(url).json()
    data = response['entries']

    return data

# @click.command()
# @click.option('-c', '--count',
#     type=click.IntRange(1, 40, clamp=True),
#     default=10,
#     help='Number of songs to show. Maximum is 40')

def print_charts(count):
    """Prints the top COUNT songs in the UK Top 40 chart."""

    data = get_charts()[:count]

    for index, element in enumerate(data, start=1):
        click.echo(
            '{}. {} - {}'.format(
                index,
                element['title'],
                element['artist'].encode('utf-8', 'replace')))

# @click.command()
# @click.option('-q', '--query',
#     type=click.STRING,
#     help='Search query')

def youtube_search(query, max_results=1):
    """Search Youtube for QUERY, returning MAX_RESULTS
        Returns a dict of video ID and TITLE mappings
    """

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
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

    videos = {search_result["snippet"]["title"]: search_result["id"]["videoId"]
    for search_result in search_response.get("items", []) 
    if search_result["id"]["kind"] == "youtube#video"}

    # print "Videos:\n"
    # for key, val in videos.items():
    #         print "ID: {} Title: {}".format(key, val), "\n"

    # Dict in format {title: id}
    return videos

def download_songs(pos):
    """Downloads the song occupying the POS spot in the charts"""

    data = get_charts()
    pos -=1
    
    search = '{} - {}'.format(
                data[pos]['title'],
                data[pos]['artist'].encode('utf-8', 'replace'))
    dl = youtube_search(search)

    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print "Downloading " + dl.keys()[0]
        ydl.download(dl.values())


if __name__ == '__main__':
    download_songs(1)
