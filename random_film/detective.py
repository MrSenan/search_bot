import urllib.parse
import requests
from random import choice
from bs4 import BeautifulSoup


def new_deaf(url, headers):

    try:
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        pagination = int(soup.find('div', id='pagination').find_all('a')[-1].text)
        page = choice([i for i in range(1, pagination + 1)])
        url_ = f'https://newdeaf.lol/genre/%D0%B4%D0%B5%D1%82%D0%B5%D0%BA%D1%82%D0%B8%D0%B2/page/{page}/'
        r = requests.get(url=url_, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        box = choice(soup.find_all('article', class_='card d-flex'))
        link = box.find('h2', class_='card__title').find('a').get('href')
        return link
    except:
        return 'Возникла ошибка..'


def lord(url, headers):
    try:
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        pagination = int(soup.find('div', class_='navigation').find_all('a')[-1].text)
        page = choice([i for i in range(1, pagination + 1)])
        url_ = f'https://lo9.lordfilm.lu/filmy/detektivy-f/page/{page}/'
        r = requests.get(url=url_, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        link = choice(soup.find_all('div', class_='th-item')).find('a').get('href')
        return link
    except:
        return 'Возникла ошибка..'


def film_hd(url, headers):
    try:
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        pagination = int(soup.find('span', class_='navigation').find_all('a')[-1].text)
        page = choice([i for i in range(1, pagination + 1)])
        url_ = f'https://vip.filmhd1080.me/detective/page/{page}/'
        r2 = requests.get(url=url_, headers=headers)
        soup2 = BeautifulSoup(r2.text, 'lxml')
        link = choice(soup2.find_all('div', class_='short nl nl2')).find('a').get('href')
        return link
    except:
        return 'Возникла ошибка..'


def hd_rezka(url, headers):
    try:
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        pagination = int(soup.find('div', class_='navigation').find_all('a')[-2].text)
        page = choice([i for i in range(1, pagination + 1)])
        url_ = f'https://nu10.hdreska.club/genres/67/{page}'
        r = requests.get(url=url_, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        link = choice(soup.find_all('div', class_='th-item')).find('a').get('href')
        percent_dec = urllib.parse.quote(link.split('~')[-1].encode('utf8'))
        res = f'https://nu10.hdreska.club{link.split("~")[0]}~{percent_dec}'
        return res
    except:
        return 'Возникла ошибка..'


def detective():
    links_arr = ['https://lo9.lordfilm.lu/filmy/detektivy-f/',
                 'https://newdeaf.lol/genre/%D0%B4%D0%B5%D1%82%D0%B5%D0%BA%D1%82%D0%B8%D0%B2/',
                 'https://vip.filmhd1080.me/detective/',
                 'https://nu10.hdreska.club/genres/67~%D0%94%D0%B5%D1%82%D0%B5%D0%BA%D1%82%D0%B8%D0%B2']

    choice_ = choice(links_arr)
    url = choice_
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/107.0.0.0 Safari/537.36'}

    if choice_ == 'https://newdeaf.lol/genre/%D0%B4%D0%B5%D1%82%D0%B5%D0%BA%D1%82%D0%B8%D0%B2/':
        return new_deaf(url, headers)
    if choice_ == 'https://lo9.lordfilm.lu/filmy/detektivy-f/':
        return lord(url, headers)
    if choice_ == 'https://vip.filmhd1080.me/detective/':
        return film_hd(url, headers)
    if choice_ == 'https://nu10.hdreska.club/genres/67~%D0%94%D0%B5%D1%82%D0%B5%D0%BA%D1%82%D0%B8%D0%B2':
        return hd_rezka(url, headers)


detective()
