import time

import requests
import telebot
from random import choice
from bs4 import BeautifulSoup
from config import token

from raiting.raiting_thriller import lord_random_film_with_need_thriller

bot = telebot.TeleBot(token)


def validation(message):
    global find_rate
    try:
        find_rate = float(message.text)
        if abs(find_rate) > 8:
            find_rate = 8
            bot.send_message(message.chat.id, 'Рейтинг фильма до 8, автоматически присваивается рейтинг 8')
            bot.send_message(message.chat.id, f'подбор фильма с рейтингом не ниже {find_rate}\nВремя поиска: 10 секунд')
            return find_rate
        else:
            bot.send_message(message.chat.id, f'подбор фильма с рейтингом не ниже {find_rate}\nВремя поиска: 10 секунд')
            return find_rate
    except ValueError:
        bot.send_message(message.chat.id, 'Только числа')
        return


def lord_find_need_rate_page(message):
    try:
        find_rate = validation(message)
        if find_rate:
            url = 'https://q.kpfilm.org/f/cat=14/sort=date/order=desc/'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                     'Chrome/107.0.0.0 Safari/537.36'}

            r = requests.get(url=url, headers=headers)
            soup = BeautifulSoup(r.text, 'lxml')
            start = time.time()
            while True:
                pagination = int(soup.find('div', class_='navigation').find_all('a')[-1].text)
                page = choice([i for i in range(pagination)])
                url2 = f'https://q.kpfilm.org/f/cat=14/sort=date/order=desc/page/{page}/'
                r2 = requests.get(url=url2, headers=headers)
                soup2 = BeautifulSoup(r2.text, 'lxml')
                valid_rate = soup2.find_all('div', class_='th-rate th-rate-imdb')
                finish = time.time() - start
                if int(finish) > 10:
                    bot.send_message(message.chat.id, '_⌛ ТАЙМАУТ ⌛_', parse_mode='Markdown')
                    break

                for v in valid_rate:
                    if len(v.text) > 1:
                        float_valid = float(v.text)
                        if float_valid >= find_rate:
                            return page, find_rate
    except:
        bot.send_message(message.chat.id, 'Выберите жанр')


def lord_random_film_with_need_rate_criminal(message):
    try:
        page_rate = lord_find_need_rate_page(message)
        url = f'https://q.kpfilm.org/f/cat=14/sort=date/order=desc/page/{page_rate[0]}/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/107.0.0.0 Safari/537.36'}

        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        films = soup.find_all('div', class_='th-item')
        films_list = []
        for film in films:
            valid_rate = film.find('div', class_='th-rate th-rate-imdb').text
            if len(valid_rate) > 1:
                float_valid = float(valid_rate)
                if float_valid >= page_rate[1]:
                    add_link = film.find('a').get('href')
                    films_list.append(add_link)

        finally_film = choice(films_list)
        res = requests.get(url=finally_film, headers=headers)
        soup2 = BeautifulSoup(res.text, 'lxml')
        finally_rate = soup2.find('div', class_='frate frate-imdb').text
        genre = soup2.find('ul', class_='flist flist-wide').find_all('li')[-1].text

        bot.send_message(message.chat.id, finally_film)
        bot.send_message(message.chat.id, f'Рейтинг imdb: {finally_rate}\n{genre}\n{"-" * 40}>')
    except Exception as e:
        bot.send_message(message.chat.id, 'Выберите жанр')
