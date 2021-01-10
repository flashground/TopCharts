import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt


europa_plus_url = 'https://europaplus.ru/top40'

def europa_plus(url):
    data = requests.get(url).text
    soup = bs(data, "html.parser")
    page_block = soup.select(".page__block")[0]
    song_list = page_block.select(".song-list .song")
    tracks = dict()
    tracks['date'] = page_block.find('div', attrs={'class':'select__label__value'}).text
    tracks['chart'] = list()
    for song in song_list:
        track = dict()
        track['singer'] = song.find('a', attrs={'class':'link'}).text
        track['song'] = song.find('p').text
        track['position'] = song.find(attrs={'class':'typography_size_min'}).text        
        tracks['chart'].append(track)
    return tracks