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

def _get_charts():
    """Retrieves the current UK Top 40 Charts"""

    url = 'http://ben-major.co.uk/labs/top40/api/singles/'
    response = requests.get(url).json()
    data = response['entries']

    return data

def _youtube_search(query, max_results=1):
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

    # Dict in format {title: id}
    return videos

@click.group()
def cli():
    """A simple command line tool to print songs in the UK Top 40 Charts
        and optionally donwloads any song in the charts 
    """
    pass

@cli.command()
@click.option('-p', '--position',
    type=click.IntRange(1, 40, clamp=True),
    help='Chart position of song to download',
    prompt=True)

def download(pos):
    """Download the song occupying the position specified"""

    data = _get_charts()
    pos -=1
    
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

@cli.command()
@click.option('-c', '--count', default=10, help='Number of Songs to Print')

def display(count):
    """Prints the songs in the chart.
       By default the top 10 songs are printed
    """

    data = _get_charts()[:count]

    for index, element in enumerate(data, start=1):
        click.echo(
            '{}. {} - {}'.format(
                index,
                element['title'],
                element['artist'].encode('utf-8', 'replace')))

if __name__ == '__main__':
    cli()
