import requests
from bs4 import BeautifulSoup as bs
from .utils import last_friday


loveradio_url = 'http://www.loveradio.ru/biglove_chart.htm'

def get_chart(url):
    tracks = dict()
    errors = []
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.text
        soup = bs(data, "html.parser")
        page_block = soup.find('table', attrs={'class':"chart__table"})
        if not page_block:
            errors.append({'url': url, 'status_code': 'page block is empty'})

        song_list = page_block.find_all('tr', attrs={'class':'chart__table-row'})
        if not song_list:
            errors.append({'url': url, 'status_code': 'song list is empty'})

        tracks['date'] = last_friday()
        tracks['chart'] = list()
        for song in song_list:
            track = dict()
            full_track_name = song.find('td', attrs={'class':'chart__table-song'}).text.split(' — ')
            if not full_track_name:
                errors.append({'url': url, 'status_code': 'full track name is empty'})
            track['singer'] = full_track_name[0].strip()
            track['song'] = full_track_name[1].strip()
            track['position'] = song.find('td', attrs={'class':'chart__table-tw'}).text
            tracks['chart'].append(track)
        return tracks, errors
    else:
        errors.append({'url': url, 'status_code': 'page do not response'})
        return tracks, errors


def main():
    chart_data = []
    chart_data.append(get_chart(loveradio_url))
    return chart_data