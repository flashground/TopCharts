import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt


loveradio_url = 'http://www.loveradio.ru/biglove_chart.htm'


def loveradio(url):
    data = requests.get(url).text
    soup = bs(data, "html.parser")
    # page_block = soup.select(".chart__table .chart__table-row")
    page_block = soup.find('table', attrs={'class':"chart__table"})
    # song_list = page_block.find_all('div', attrs={'class':'chart__table-row'})
    song_list = page_block.find_all('tr', attrs={'class':'chart__table-row'})
    tracks = dict()
    # tracks['date'] = page_block.find('div', attrs={'class':'select__label__value'}).text
    tracks['chart'] = list()
    for song in song_list:
        track = dict()
        song1 = song.find('td', attrs={'class':'chart__table-song'}).text.split(' — ')
        track['singer'] = song1[0].strip()
        track['song'] = song1[1].strip()
        track['position'] = song.find('td', attrs={'class':'chart__table-tw'}).text      
        tracks['chart'].append(track)
    return tracks