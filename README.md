# Top 40

A simple command line program that displays songs in the current UK Top 40 Charts
This also displays their YouTube links for convenience.

## Install

`git clone https://github.com/kevgathuku/top40`  
`cd top40`  
`pip install -r requirements.txt`


## Setup
If you just need to display the songs without the YouTube links, no additional action is required.  
You can skip ahead to the Usage section.

If you require to view the songs and their YouTube links:    

Obtain a developer key from [Google](https://developers.google.com/youtube/registering_an_application)
This is required for accessing the YouTube API.

Set the developer key as an environment variable:  
    `export DEVELOPER_KEY="Your developer key"`

## Usage

There is just one basic command to display the songs:

`top40 display [OPTIONS]`  

### Displaying Songs

Example usage:

    `top40 display`                   No arguments given. Displays the top 10 songs in the Charts.
    `top40 display -n 30`             This displays the top 30 songs in the chart
    `top40 display -n 30  --links`    This displays the top 30 songs in the chart and their YouTube links

#### OPTIONS
    -h, --help                        print this help text and exit
    -n, --num                         Specify the number of songs to display. Maximum of 40

## Help

`top40 --help`
