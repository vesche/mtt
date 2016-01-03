#!/usr/bin/env python
# movietv.to scraper command line utility

import click
import re
import requests
import subprocess
import sys
from bs4 import BeautifulSoup

token_pattern = re.compile(r'var token_key="(.*?)";')

@click.group()
def cli():
    pass

@cli.command()
@click.option('--movie', help='Name of movie to find.')
@click.option('--quality', type=click.Choice(['All', '720p', '1080p']), help='Quality of movies.')
def run(movie, quality):
    with requests.Session() as session:
        session.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; \
        Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'}

        # extract token
        response = session.get('http://movietv.to/')
        soup = BeautifulSoup(response.content, 'html.parser')

        script = soup.find('script', text=token_pattern).get_text()
        match = token_pattern.search(script)
        if not match:
            raise ValueError('Cannot find token!')
        token = match.group(1)

        # search for the movies
        response = session.post('http://movietv.to/index/loadmovies', data={
            'loadmovies': 'showData',
            'page': '1',
            'abc': 'All',
            'genres': '',
            'sortby': 'Popularity',
            'quality': quality,
            'type': 'movie',
            'q': movie,
            'token': token
        })

        soup = BeautifulSoup(response.content, 'html.parser')

        movie_links = []
        movies = []
        for link in soup.find_all('a'):
            movie_links.append(link.get('href'))
        for link in soup.find_all('h2'):
            movies.append(link.text)

        for n in range(len(movies)):
            print '{0}. {1}'.format(n+1, movies[n])
        movie_numb = click.prompt('Movie #?', type=int)

        response = session.get('http://movietv.to/{}'.format(movie_links[movie_numb-1]))
        soup = BeautifulSoup(response.content, 'html.parser')

        for stream in soup.find_all('source'):
            stream_link = stream.get('src')
        stream_link = '&'.join(stream_link.split('&')[:3])

        if sys.platform == 'win32':
            try:
                subprocess.Popen(['C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe', stream_link])
            except:
                subprocess.Popen(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe', stream_link])
        else:
            subprocess.Popen(['vlc', stream_link])

if __name__ == '__main__':
    run()
