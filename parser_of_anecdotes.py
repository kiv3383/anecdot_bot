# import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

from database.core import crud
from database.models import db, Anecdotes
from message_sender import bot

URL = 'https://www.anekdot.ru/last/good/'
PATH = 'C:/Users/USER/PycharmProjects/anecdot_bot/venv/Scripts/node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs.exe'

db_write = crud.create()
db_clear = crud.clear()


# def parser_from_requests(url: str) -> None:
#     """
#     Парсит текст с помощью  requests из тега div в список, сохраняет в файл.
#     При ошибке соединения отправляет ошибку пользователю.
#     """
#     try:
#         req = requests.get(url)
#         if req.status_code != 200:
#             raise Exception
#         soup = bs(req.text, 'html.parser')
#         anecdotes = soup.find_all(['div'], class_=['text'])
#         list_of_anecdotes = [anecdote.text for anecdote in anecdotes]
#         with open('anecdotes.txt', 'w+', encoding='utf-8') as file:
#             for elem in list_of_anecdotes:
#                 file.write(elem + '\n')
#     except Exception as er:
#         bot.send_message(chat_id=6377827844, text=er)
#         with open('anecdotes.txt', 'w+', encoding='utf-8') as file:
#             file.truncate(0)


# parser_from_requests(url=URL)


def parser_from_selenium(url: str) -> None:
    """
        Парсит текст и рейтинг с помощью selenium, сортирует по рейтингу, сохраняет в бд.
        При ошибке отправляет оповещение пользователю.
        """
    anecdotes_list = []
    browser = webdriver.Chrome()
    browser.get(url)
    html = browser.page_source
    soup = bs(html, 'html.parser')

    block = soup.find_all('div', class_='topicbox', id=True)
    for elem in block:
        for br in elem.select('br'):
            br.replace_with('\n')
        anecdote = elem.find('div', class_='text').text
        anecdote_rate = elem.find(class_="value")
        anecdotes = {
            'anecdote': anecdote,
            'anecdote_rate': int(anecdote_rate.text),
            'publication': True
        }
        anecdotes_list.append(anecdotes)
        anecdotes_list.sort(key=lambda el: el['anecdote_rate'], reverse=True)

        print(anecdotes_list)

        db_clear(db, Anecdotes)
        db_write(db, Anecdotes, anecdotes_list)


parser_from_selenium(url=URL)
