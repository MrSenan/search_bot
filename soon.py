import requests
from random import choice
from bs4 import BeautifulSoup
from config import token
from telebot import TeleBot

bot = TeleBot(token)


def soon(message):
    url = 'https://www.film.ru/soon'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/107.0.0.0 Safari/537.36'}
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    random_film = choice(soup.find_all('div', class_='film_catalog'))
    link = f'https://www.film.ru/{random_film.find("a").get("href")}'
    bot.send_message(message.chat.id, link)

    r2 = requests.get(url=link, headers=headers)
    soup2 = BeautifulSoup(r2.text, 'lxml')

    info = soup2.find('div', class_='movies-center-table').find_all('strong')
    info2 = soup2.find('div', class_='movies-center-table').find_all('div', class_='h3')

    genres = soup2.find('div', class_='movies-center').find('div', class_='h3').find_all('a')
    genres_arr = [i.text.strip() for i in genres]
    bot.send_message(message.chat.id, ',  '.join(genres_arr))

    res = [i for i in zip(info, info2)]
    for i in res:
        bot.send_message(message.chat.id, f'{i[1].text.strip()} : {i[0].text.strip()}')


