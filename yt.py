import os
import sys
import time

import telebot
from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
from config import token

bot = telebot.TeleBot(token)


def download_from_links(message):
    try:
        url = message.text
        yt = YouTube(url, on_progress_callback=on_progress)
    except:
        bot.send_message(message.chat.id, 'не правильный формат ссылки')
    else:
        try:
            syms = ('!"#$%&()*+,-./:;<=>?@[\]^_`{|}~')
            video_name = ''.join([c for c in yt.title if c not in syms]) + '.mp4'
            path = r'C:\Users\Пк\PycharmProjects\newdeaf\video'
            # path = '/home/newdeaf/video'
            stream = yt.streams.get_by_itag(22)
            stream.download(path, video_name)
            # print(message.video[0].file_id)
            # if os.stat(fr'{path}/{name}').st_size // 10 ** 6 > 50:
            if os.stat(fr'{path}\{video_name}').st_size // 10 ** 6 > 50:
                bot.send_message(message.chat.id, 'весит больше 50 мб')
                # os.remove(path + '/' + name)
                os.remove(path + '\\' + video_name)
                sys.exit()

            # video = open(fr'{path}/{name}', 'rb')
            video = open(fr'{path}\{video_name}', 'rb')
            bot.send_message(message.chat.id, yt.title)
            # bot.get_file(message.chat.id)
            bot.send_video(message.chat.id, video, parse_mode='Markdown')
            video.close()
            # os.remove(path + '/' + name)
            os.remove(path + '\\' + video_name)
        except Exception as e:
            bot.send_message(message.chat.id, e)


