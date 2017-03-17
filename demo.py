# !/usr/bin/python
# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

class getMusic(object):
    def __init__(self, url):
        self.play_url = url
        self.s = requests.session()
        self.headers = {
            'Referer': 'http://music.163.com/',
            'Host': 'music.163.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        }

    def get_music_id (self):
        s = BeautifulSoup(self.s.get(self.play_url, headers = self.headers).content, 'html.parser')

        main = s.find('ul', {'class':'f-hide'})

        for music in main.find_all('a'):
            musicId = music['href'].replace('/song?id=', '');
            print music.text, self.change(musicId)

    def change (self, musicId):
        url = 'http://music.163.com/api/song/detail/?id='+musicId+'&ids=%5B'+musicId+'%5D&csrf_token='
        content = self.s.get(url).content
        mp3Url = re.search(r'"mp3Url":"(.*?)"', content)

        return mp3Url.group(1)

if __name__ == '__main__':
    url = 'http://music.163.com/playlist?id=629923019'
    a = getMusic(url)
    a.get_music_id()









