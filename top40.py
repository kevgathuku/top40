#/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import requests
import requests_cache

# Cache the API calls and expire after 12 hours
requests_cache.install_cache(expire_after=43200)

url = 'http://ben-major.co.uk/labs/top40/api/singles/'

@click.command()
@click.option('--count',
    type=click.IntRange(1, 40, clamp=True),
    default=10,
    help='Number of songs to show. Maximum is 40')

def get_charts(count):
    """Prints the top COUNT songs in the UK Top 40 chart."""

    response = requests.get(url).json()
    data = response['entries'][:count]
    for index, element in enumerate(data, start=1):
        click.echo(
            '{}. {} - {}'.format(
                index,
                element['title'],
                element['artist'].encode('utf-8', 'replace')))

if __name__ == '__main__':
    get_charts()

