import requests
from bs4 import BeautifulSoup as bs
from .utils import convert_date


europaplus_url = 'https://europaplus.ru/top40'

def main(url=europaplus_url):
    tracks = dict()
    errors = []

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.text
        soup = bs(data, "html.parser")
        page_block = soup.select(".page__block")[0]
        if not page_block:
            errors.append({'url': url, 'status_code': 'page block is empty'})
        song_list = page_block.select(".song-list .song")
        if not song_list:
            errors.append({'url': url, 'status_code': 'song list is empty'})
        date_str = page_block.find('div', attrs={'class':'select__label__value'}).text.split(' - ')[0]
        if not date_str:
            errors.append({'url': url, 'status_code': 'date str is empty'})
        tracks['date'] = convert_date(date_str)
        tracks['chart'] = list()
        song_list.reverse()
        for song in song_list:
            track = dict()
            track['singer'] = song.find('a', attrs={'class':'link'}).text
            track['song'] = song.find('p').text
            track['position'] = song.find(attrs={'class':'typography_size_min'}).text
            tracks['chart'].append(track)
        return tracks, errors

    else:
        errors.append({'url': url, 'status_code': 'page do not response'})
    return tracks, errors
