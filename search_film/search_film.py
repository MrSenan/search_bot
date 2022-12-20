import time

import requests
import telebot
from bs4 import BeautifulSoup
from telebot import types

from config import token
import urllib.parse

from soon import soon

bot = telebot.TeleBot(token)


def rand_films_menu(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='🪓 Ужасы')
    btn2 = types.KeyboardButton(text='🩸 Триллер')
    btn3 = types.KeyboardButton(text='🕵 Детектив')
    btn4 = types.KeyboardButton(text='🕶 Криминал')
    btn5 = types.KeyboardButton(text='💂‍♂️ Военные')
    btn6 = types.KeyboardButton(text='💥 Боевик')
    btn7 = types.KeyboardButton(text='🤣 Комедия')
    btn8 = types.KeyboardButton(text='🔮 Фантастика')
    btn9 = types.KeyboardButton(text='🏡 Меню')
    kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    bot.send_message(message.chat.id, 'Случайный фильм на вечер\nВыберете жанр', reply_markup=kb)


def rating_menu(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='🪓 Рейтинг Ужасы')
    btn2 = types.KeyboardButton(text='🩸 Рейтинг Триллер')
    btn3 = types.KeyboardButton(text='🕵 Рейтинг Детектив')
    btn4 = types.KeyboardButton(text='🕶 Рейтинг Криминал')
    btn5 = types.KeyboardButton(text='💂‍♂️ Рейтинг Военные')
    btn6 = types.KeyboardButton(text='💥 Рейтинг Боевик')
    btn7 = types.KeyboardButton(text='🤣 Рейтинг Комедия')
    btn8 = types.KeyboardButton(text='🔮 Рейтинг Фантастика')
    btn9 = types.KeyboardButton(text='🏡 Меню')
    kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    bot.send_message(message.chat.id, 'Категория выбора рейтинга', reply_markup=kb)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='🔎 Поиск фильма')
    btn2 = types.KeyboardButton(text='❓ Случайный фильм на вечер')
    btn3 = types.KeyboardButton(text='🏆 Фильм с выбором рейтинга')
    btn4 = types.KeyboardButton(text='📅 Ближайшие кинопремьеры')
    btn5 = types.KeyboardButton(text='🏡 Меню')
    # btn4 = types.KeyboardButton(text='Скачать с YT')
    kb.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, '🏡 Меню', reply_markup=kb)


def search_film(message):
    film_name = str(message.text)
    if film_name == '🏡 Меню':
        return start(message)
    if message.text == '❓ Случайный фильм на вечер':
        return rand_films_menu(message)
    if message.text == '🏆 Фильм с выбором рейтинга':
        return rating_menu(message)
    if message.text == '📅 Ближайшие кинопремьеры':
        return soon(message)
    bot.send_message(message.chat.id, 'поиск по "hdreska"')
    url = f'https://nu10.hdreska.club/search?do=search&subaction=search&q={film_name}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/107.0.0.0 Safari/537.36'}
    try:
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        film_url = soup.find_all('div', class_='th-item')
        films_list = []
        for film in film_url:
            href = film.find('a').get('href')
            percent_dec = urllib.parse.quote(film_name.encode('utf8'))
            url_ = href.split('~')[0]
            res = f'https://nu10.hdreska.club{url_}~{percent_dec}'
            films_list.append(res)
        if len(films_list) == 0:
            search_film_lord(message, film_name)
        elif len(films_list) == 1:
            for i in films_list:
                bot.send_message(message.chat.id, i)
        elif len(films_list) > 1:
            bot.send_message(message.chat.id, f'Найдено {len(films_list)} совпадений с запросом {film_name}')
            time.sleep(1)
            for i in films_list:
                bot.send_message(message.chat.id, i)
    except:
        bot.send_message(message.chat.id, 'Возникла проблема!!')


def search_film_lord(message, name):
    bot.send_message(message.chat.id, 'поиск по "lordfilm"')
    try:
        url = 'https://hd.kpfilm.org/index.php?do=search'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/107.0.0.0 Safari/537.36'}
        data = {'do': 'search',
                'subaction': 'search',
                'search_start': 0,
                'full_search': 0,
                'result_from': 1,
                'story': name
                }
        r = requests.post(url=url, headers=headers, data=data)
        soup = BeautifulSoup(r.text, 'lxml')
        film_url = soup.find_all('div', class_='th-item')
        films_list = []
        for film in film_url:
            href = film.find('a').get('href')
            films_list.append(href)
        if len(films_list) == 0:
            hd_film(message, name)
        elif len(films_list) == 1:
            for i in films_list:
                bot.send_message(message.chat.id, i)
        else:
            bot.send_message(message.chat.id, f'Найдено {len(films_list)} совпадений с запросом {name}')
            time.sleep(1)
            for i in films_list:
                bot.send_message(message.chat.id, i)
    except:
        bot.send_message(message.chat.id, 'Возникла проблема')


def hd_film(message, name):
    bot.send_message(message.chat.id, 'поиск по "hdfilm"')
    try:
        url = 'https://vip.filmhd1080.buzz/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/107.0.0.0 Safari/537.36'}
        data = {'do': 'search',
                'subaction': 'search',
                'story': name
                }
        r = requests.post(url=url, headers=headers, data=data)
        soup = BeautifulSoup(r.text, 'lxml')
        film_url = soup.find_all('div', class_='kratka-in')
        films_list = []
        for film in film_url:
            href = film.find('a').get('href')
            films_list.append(href)
        if len(films_list) == 0:
            bot.send_message(message.chat.id, 'Ничего не найдено')
        elif len(films_list) == 1:
            for i in films_list:
                bot.send_message(message.chat.id, i)
        else:
            bot.send_message(message.chat.id, f'Найдено {len(films_list)} совпадений с запросом {name}')
            time.sleep(1)
            for i in films_list:
                bot.send_message(message.chat.id, i)
    except:
        bot.send_message(message.chat.id, 'Возникла проблема')
