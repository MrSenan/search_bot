import telebot
from telebot import types

from config import token


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


def validation(message):
    find_rate = message.text
    if find_rate == '🏡 Меню':
        start(message)
        return False
    else:
        find_rate = float(find_rate)
    try:
        if abs(float(find_rate)) > 8:
            find_rate = 8
            bot.send_message(message.chat.id, 'Рейтинг фильма до 8, автоматически присваивается рейтинг 8')
            bot.send_message(message.chat.id, f'подбор фильма с рейтингом не ниже {find_rate}\nВремя поиска: 10 секунд')
            return find_rate
        else:
            bot.send_message(message.chat.id, f'подбор фильма с рейтингом не ниже {find_rate}\nВремя поиска: 10 секунд')
            return find_rate
    except ValueError:
        bot.send_message(message.chat.id, 'Только числа\nНажмите кнопку выбора жанра повторно')
