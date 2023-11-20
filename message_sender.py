from dotenv import load_dotenv

import telebot

from config import AllSettings
from database.core import crud
from database.models import db, Anecdotes

settings = AllSettings()

load_dotenv()

bot = telebot.TeleBot(settings.bot_token.get_secret_value())
db.read = crud.retrieve()
db.delete = crud.delete_by_id()


def read_send_from_file() -> None:
    """Читает первую строку файла, отправляет, удаляет строку из файла."""
    with open("anecdotes.txt", "r+", encoding="utf-8") as file_anecdotes:
        anecdotes = file_anecdotes.readlines()
        file_anecdotes.truncate(0)
        file_anecdotes.seek(0)
        file_anecdotes.writelines(anecdotes[1:])

    for channel in settings.tg_channels:
        bot.send_message(channel,
                         anecdotes[0],
                         disable_notification=True,
                         disable_web_page_preview=True,
                         parse_mode='HTML')


def read_send_from_bd():
    anecdotes = db.read(db, Anecdotes)
    try:
        for channel in settings.tg_channels:
            bot.send_message(channel,
                             anecdotes[0].anecdote,
                             disable_notification=True,
                             disable_web_page_preview=True,
                             parse_mode='HTML')
        db.delete(db, Anecdotes, anecdotes[0])
    except IndexError as er:
        text = 'Ошибка: вернулся пустой список анекдотов из бд. ' + str(er)
        bot.send_message(chat_id=int(settings.my_chat_id.get_secret_value()), text=text)


if __name__ == '__main__':
    # read_send_from_file()
    read_send_from_bd()
