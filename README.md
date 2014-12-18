# Top 40

A simple command line program that prints and optionally downloads
the UK Top 40 singles charts

## Setup
Obtain a developer key from [Google](https://developers.google.com/youtube/registering_an_application)
This is required for accessing the YouTube API.

Rename the provided .env.example file to .env
Open up the .env file and set the developer key you obtained from Google
`export DEVELOPER_KEY="Your developer key"`

## Install

`git clone https://github.com/kevgathuku/top40`  
`cd top40`  
`pip install -r requirements.txt`

## Usage

There are two basic commands:

`top40 display [OPTIONS]`  
`top40 download [OPTIONS]`

### Displaying Songs

Example usage:

`top40 display -n 30`            This displays the top 30 songs in the chart

#### OPTIONS
    -h, --help                   print this help text and exit
    -n, --num                    Specify the number of songs to display. Maximum of 40

### Downloading a song

`top40 download [OPTIONS]`

#### OPTIONS
    -h, --help                   print this help text and exit
    -p, --pos                    Position in the chart of the song to download

## Help

`top40 --help`

## Disclaimer:
Check your local copyright laws before using this tool to download music
