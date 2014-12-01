# Top 40

A simple command line program that prints and optionally downloads
the UK Top 40 singles charts

## Setup
Obtain a developer key from [Google](https://developers.google.com/youtube/registering_an_application)  
export DEVELOPER_KEY="Your developer key"

## Install

`git clone https://github.com/kevgathuku/top40`  
`cd top40`  
`pip install -r requirements.txt`

## Usage

`top40 display [OPTIONS]`

### OPTIONS
    -h, --help                   print this help text and exit
    -c, --count                  Number of songs to display. Maximum of 40

`top40 download [OPTIONS]`

### OPTIONS
    -h, --help                   print this help text and exit
    -p, --pos                    Position in the chart of the song to download

## Help

`top40 --help`

## Disclaimer:
Check your local copyright laws before using this tool to download music
