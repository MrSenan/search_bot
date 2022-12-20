import os
import sys
import time
from time import sleep
import telebot

from telebot import types

from config import token

from soon import soon
from search_film.search_film import search_film

from random_film.horror import horror
from random_film.thriller import thriller
from random_film.detective import detective
from random_film.criminal import criminal
from random_film.war import war
from random_film.action_movie import action_movie
from random_film.comedy import comedy
from random_film.fantasy import fantasy
from random_film.history import history
from random_film.drama import drama

from raiting.raiting_horror import lord_random_film_with_need_rate_horror
from raiting.raiting_thriller import lord_random_film_with_need_thriller
from raiting.raiting_detective import lord_random_film_with_need_rate_detective
from raiting.raiting_criminal import lord_random_film_with_need_rate_criminal
from raiting.raiting_war import lord_random_film_with_need_rate_war
from raiting.raiting_action_movie import lord_random_film_with_need_rate_action_movie
from raiting.raiting_comedy import lord_random_film_with_need_rate_comedy
from raiting.raiting_fantasy import lord_random_film_with_need_rate_fantasy
from raiting.raiting_history import lord_random_film_with_need_rate_history
from raiting.raiting_drama import lord_random_film_with_need_rate_drama

from yt import download_from_links

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
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


@bot.message_handler(content_types=['text', 'video'])
def action(message):
    if message.text == '🏡 Меню':
        start(message)

    if message.text == '📅 Ближайшие кинопремьеры':
        bot.send_message(message.chat.id, '⬆️Подбор ближайшей премьеры⬆️', soon(message))

    if message.text == '🔎 Поиск фильма':
        # kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        # btn1 = types.KeyboardButton(text='🔎 Поиск фильма')
        # btn2 = types.KeyboardButton(text='🏡 Меню')
        # kb.add(btn1, btn2)
        bot.send_message(message.chat.id, '🔎 Введите название фильма ⬇️⬇️⬇️')
        bot.register_next_step_handler(message, search_film)

    # Кнопка Случайный фильм на вечер СТАРТ
    if message.text == '❓ Случайный фильм на вечер':
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton(text='🪓 Ужасы')
        btn2 = types.KeyboardButton(text='🩸 Триллер')
        btn3 = types.KeyboardButton(text='🕵 Детектив')
        btn4 = types.KeyboardButton(text='🕶 Криминал')
        btn5 = types.KeyboardButton(text='💂‍♂️ Военные')
        btn6 = types.KeyboardButton(text='💥 Боевик')
        btn7 = types.KeyboardButton(text='🤣 Комедия')
        btn8 = types.KeyboardButton(text='🔮 Фантастика')
        btn9 = types.KeyboardButton(text='🗡 Исторический')
        btn10 = types.KeyboardButton(text='😔 Драма')
        btn11 = types.KeyboardButton(text='🏡 Меню')
        kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        bot.send_message(message.chat.id, 'Случайный фильм на вечер\n\nВыберите жанр', reply_markup=kb)

    if message.text == '🪓 Ужасы':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, '🪓 Подбор в жанре ужасы ')
        bot.send_message(message.chat.id, horror())
    if message.text == '🩸 Триллер':
        bot.send_message(message.chat.id, 'Подбор в жанре триллер')
        bot.send_message(message.chat.id, thriller())
    if message.text == '🕵 Детектив':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Подбор в жанре детектив')
        bot.send_message(message.chat.id, detective())
    if message.text == '🕶 Криминал':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Подбор в жанре Криминал')
        bot.send_message(message.chat.id, criminal())
    if message.text == '💂‍♂️ Военные':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Подбор в жанре Военные')
        bot.send_message(message.chat.id, war())
    if message.text == '💥 Боевик':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Подбор в жанре Боевик')
        bot.send_message(message.chat.id, action_movie())
    if message.text == '🤣 Комедия':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Подбор в жанре Комедия')
        bot.send_message(message.chat.id, comedy())
    if message.text == '🔮 Фантастика':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Подбор в жанре Фантастика')
        bot.send_message(message.chat.id, fantasy())
    if message.text == '🗡 Исторический':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Подбор в жанре Исторический')
        bot.send_message(message.chat.id, history())
    if message.text == '😔 Драма':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Подбор в жанре Драма')
        bot.send_message(message.chat.id, drama())
    # Кнопка Случайный фильм на вечер КОНЕЦ

    # Кнопка Фильм с выбором рейтинга СТАРТ
    if message.text == '🏆 Фильм с выбором рейтинга':
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton(text='🪓 Рейтинг Ужасы')
        btn2 = types.KeyboardButton(text='🩸 Рейтинг Триллер')
        btn3 = types.KeyboardButton(text='🕵 Рейтинг Детектив')
        btn4 = types.KeyboardButton(text='🕶 Рейтинг Криминал')
        btn5 = types.KeyboardButton(text='💂‍♂️ Рейтинг Военные')
        btn6 = types.KeyboardButton(text='💥 Рейтинг Боевик')
        btn7 = types.KeyboardButton(text='🤣 Рейтинг Комедия')
        btn8 = types.KeyboardButton(text='🔮 Рейтинг Фантастика')
        btn9 = types.KeyboardButton(text='🗡 Рейтинг Исторический')
        btn10 = types.KeyboardButton(text='😔 Рейтинг Драма')
        btn11 = types.KeyboardButton(text='🏡 Меню')
        kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        bot.send_message(message.chat.id, 'Категория выбора рейтинга', reply_markup=kb)

    if message.text == '🪓 Рейтинг Ужасы':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Укажите рейтинг для поиска в жанре Ужасы ⬇️⬇️⬇️')
        bot.register_next_step_handler(message, lord_random_film_with_need_rate_horror)
    if message.text == '🩸 Рейтинг Триллер':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Укажите рейтинг для поиска в жанре Триллер⬇️⬇️⬇️')
        bot.register_next_step_handler(message, lord_random_film_with_need_thriller)
    if message.text == '🕵 Рейтинг Детектив':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Укажите рейтинг для поиска в жанре Детектив⬇️⬇️⬇️')
        bot.register_next_step_handler(message, lord_random_film_with_need_rate_detective)
    if message.text == '🕶 Рейтинг Криминал':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Укажите рейтинг для поиска в жанре Криминал⬇️⬇️⬇️')
        bot.register_next_step_handler(message, lord_random_film_with_need_rate_criminal)
    if message.text == '💂‍♂️ Рейтинг Военные':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Укажите рейтинг для поиска в жанре Военные⬇️⬇️⬇️')
        bot.register_next_step_handler(message, lord_random_film_with_need_rate_war)
    if message.text == '💥 Рейтинг Боевик':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Укажите рейтинг для поиска в жанре Боевик⬇️⬇️⬇️')
        bot.register_next_step_handler(message, lord_random_film_with_need_rate_action_movie)
    if message.text == '🤣 Рейтинг Комедия':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Укажите рейтинг для поиска в жанре Комедия⬇️⬇️⬇️')
        bot.register_next_step_handler(message, lord_random_film_with_need_rate_comedy)
    if message.text == '🔮 Рейтинг Фантастика':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Укажите рейтинг для поиска в жанре Фантастика⬇️⬇️⬇️')
        bot.register_next_step_handler(message, lord_random_film_with_need_rate_fantasy)
    if message.text == '🗡 Рейтинг Исторический':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Укажите рейтинг для поиска в жанре Исторический⬇️⬇️⬇️')
        bot.register_next_step_handler(message, lord_random_film_with_need_rate_history)
    if message.text == '😔 Рейтинг Драма':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, 'Укажите рейтинг для поиска в жанре Драма⬇️⬇️⬇️')
        bot.register_next_step_handler(message, lord_random_film_with_need_rate_drama)
    # Кнопка Фильм с выбором рейтинга КОНЕЦ

    # if message.text == 'Скачать с YT':
    #     bot.send_message(message.chat.id, f'введите ссылку для скачивания')
    #     # bot.send_message(message.chat.id, message.video.file_id)
    #     bot.register_next_step_handler(message, download_from_links)


def restart():
    while True:
        try:
            bot.infinity_polling()
        except:
            sleep(1)
            bot.infinity_polling()


restart()
