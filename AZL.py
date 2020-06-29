from bs4 import BeautifulSoup
import json
import requests
import time
import re
import random
from setup_request import user_agents
from pprint import pprint

site_AZL = 'https://www.azlyrics.com/'

# Return all songs organized by albums from an artist
def getJSON(artist): 
    discography = {
        'artist': artist,
        'albums': [],
        'total_albums' : 0
    }
    artist = re.sub('[^A-Za-z0-9]+','',artist)

    #Check if artist starts with a digit bc of different endpoint
    if(artist[0].isdigit()): charIndex = '19'
    else: charIndex = artist[0].lower()

    # Create artist endpoint
    url = site_AZL + charIndex + '/' + artist.lower() + '.html'
    # Enter artist page
    page = requests.get(url, headers={'User-Agent': random.choice(user_agents)})
    pprint(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    html_album_list = soup.select('div[id="listAlbum"]')[0]
    album_tags = html_album_list.select('div[class="album"]')
    # At each album it will get the list of songs below it in the html
    for album_tag in album_tags:
        album_name = album_tag.select('b')[0].getText().strip('"')
        print('Album: ' + album_name)
        album = {
            'album_title': album_name,
            'songs' : [],
            'total_songs' : 0
        }
        song_tags = album_tag.find_next_siblings(['div'])
        song_list = []
        for song_tag in song_tags:
            if(song_tag['class'][0] == 'album'):
                break
            song_name = song_tag.getText()
            song_info = {
                'song_title':song_name,
                'lyrics' : ''
            }
            # Create song endpoint
            song_alias = re.sub('[^A-Za-z0-9]+','',song_name)
            url = site_AZL + 'lyrics/' + artist.lower() + '/' + song_alias.lower() + '.html'
            secs = [10,12,15]
            time.sleep(random.choice(secs))

            # Enter song page
            print(url)
            page = requests.get(url, headers={'User-Agent': random.choice(user_agents)})
            soup = BeautifulSoup(page.text, 'html.parser')
            html_lyrics = soup.find_all('div', attrs={'class': None, 'id': None})
            lyrics = [l.getText().strip() for l in html_lyrics]
            if lyrics:
                song_info['lyrics'] = lyrics
                song_list.append(song_info)
            pprint(song_info)
        album['songs'] = song_list
        album['total_songs'] = len(album['songs'])
        discography['albums'].append(album)
    discography['total_albums'] = len(discography['albums'])
    
    return discography
    