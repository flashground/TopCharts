import requests
from bs4 import BeautifulSoup as bs
from .utils import convert_date, get_old_charts


WEEKS = 4

europaplus_url = 'https://europaplus.ru/top40'

def get_chart(url):
    tracks = dict()
    errors = []
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.text
        soup = bs(data, "html.parser")
        page_block = soup.select(".page__block")[0]
        if not page_block:
            errors.append({'url': url, 'status_code': 'page block is empty'})
            return tracks, errors

        song_list = page_block.select(".song-list .song")
        if not song_list[0].text:
            errors.append({'url': url, 'status_code': 'song list is empty'})
            return tracks, errors

        date_str = page_block.find('div', attrs={'class': 'select__label__value'}).text.split(' - ')[0]
        if not date_str:
            errors.append({'url': url, 'status_code': 'date str is empty'})
            return tracks, errors

        tracks['date'] = convert_date(date_str)
        tracks['chart'] = list()
        song_list.reverse()
        for song in song_list:
            track = dict()
            track['singer'] = song.find('a', attrs={'class': 'link'}).text
            track['song'] = song.find('p').text
            track['position'] = song.find(attrs={'class': 'typography_size_min'}).text
            tracks['chart'].append(track)
        return tracks, errors

    else:
        errors.append({'url': url, 'status_code': 'page do not response'})
    return tracks, errors


def main(main_url = europaplus_url, last_weeks=WEEKS):
    week_list = get_old_charts(last_weeks)
    chart_data = []
    for week in week_list:
        url = europaplus_url + '?date=' + week
        chart_data.append(get_chart(url))
    return chart_data




