import click
import requests

url = 'http://ben-major.co.uk/labs/top40/api/singles/'

response = requests.get(url)

print response.json()
