import telebot
from config import token
bot = telebot.TeleBot(token)
import requests
from bs4 import BeautifulSoup

HELP_MESSAGE = 'Введи свой знак зодиака и узнай что тебя ждет...'
UNKNOWN_COMMAND_MESSAGE = 'Звезды не всемогущи, они не могут дать ответ на это(\n Напиши /help.'
START_MESSAGE = 'Загляни в свое будущее...'

match = {
    'aries': ['овен', 'aries'],
    'taurus': ['телец', 'taurus'],
    'gemini': ['близнец', 'близнецы', 'twin', 'twins', 'gemini'],
    'cancer': ['рак', 'cancer'],
    'leo': ['лев', 'leo'],
    'virgo': ['дева', 'virgo'],
    'libra': ['весы', 'libra'],
    'scorpio': ['скорпион', 'scorpio'],
    'sagittarius': ['стрелец', 'sagittarius'],
    'capricorn': ['козерог', 'capricorn'],
    'aquarius': ['водолей', 'aquarius'],
    'pisces': ['рыбы', 'pisces']
}

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    command = message.text.lower()
    zodiac = None
    for key, commands in match.items():
        if command in commands:
            zodiac = key
            break

    if zodiac is not None:
        msg = getHoroscope(zodiac)
    elif command == "/help":
        msg = HELP_MESSAGE
    else:
         msg = UNKNOWN_COMMAND_MESSAGE
    bot.send_message(message.from_user.id, msg)


def getHoroscope(zodiac):
    SITE = 'https://horo.mail.ru/prediction/' + zodiac + '/today/'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
    full_page = requests.get(SITE, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "article__item article__item_alignment_left article__item_html"})
    return convert[0].text

bot.polling(none_stop=True, interval=0)