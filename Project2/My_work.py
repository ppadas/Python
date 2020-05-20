import telebot
bot = telebot.TeleBot('1070560085:AAEEKfyf1VfXO1lBT1ekMk-BuG8OF7gAcHk')
import requests
from bs4 import BeautifulSoup

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Введи свой знак зодиака и узнай что тебя ждет...")
    elif message.text.lower() == "овен" or message.text.lower() == "aries":
        SITE = 'https://horo.mail.ru/prediction/aries/today/'
        bot.send_message(message.from_user.id, getHoroscope(SITE))
    elif message.text.lower() == "телец" or message.text.lower() == "taurus ":
        SITE = 'https://horo.mail.ru/prediction/taurus/today/'
        bot.send_message(message.from_user.id, getHoroscope(SITE))
    elif message.text.lower() == "близнец" or message.text == "близнецы" or message.text == "twins" \
            or message.text == "twin":
        SITE = 'https://horo.mail.ru/prediction/gemini/today/'
        bot.send_message(message.from_user.id, getHoroscope(SITE))
    elif message.text.lower() == "рак" or message.text == "cancer":
        SITE = 'https://horo.mail.ru/prediction/cancer/today/'
        bot.send_message(message.from_user.id, getHoroscope(SITE))
    elif message.text.lower() == "лев" or message.text.lower() == "leo":
        SITE = 'https://horo.mail.ru/prediction/leo/today/'
        bot.send_message(message.from_user.id, getHoroscope(SITE))
    elif message.text.lower() == "дева" or message.text.lower() == "virgo":
        SITE = 'https://horo.mail.ru/prediction/virgo/today/'
        bot.send_message(message.from_user.id, getHoroscope(SITE))
    elif message.text.lower() == "весы" or message.text.lower() == "libra":
        SITE = 'https://horo.mail.ru/prediction/libra/today/'
        bot.send_message(message.from_user.id, getHoroscope(SITE))
    elif message.text.lower() == "скорпион" or message.text.lower() == "scorpio":
        SITE = 'https://horo.mail.ru/prediction/scorpio/today/'
        bot.send_message(message.from_user.id, getHoroscope(SITE))
    elif message.text.lower() == "стрелец" or message.text.lower() == "sagittarius":
        SITE = 'https://horo.mail.ru/prediction/sagittarius/today/'
        bot.send_message(message.from_user.id, getHoroscope(SITE))
    elif message.text.lower() == "козерог" or message.text.lower() == "capricorn":
        SITE = 'https://horo.mail.ru/prediction/capricorn/today/'
        bot.send_message(message.from_user.id, getHoroscope(SITE))
    elif message.text.lower() == "водолей" or message.text.lower() == "aquarius":
        SITE = 'https://horo.mail.ru/prediction/aquarius/today/'
        bot.send_message(message.from_user.id, getHoroscope(SITE))
    elif message.text.lower() == "рыбы" or message.text.lower() == "pisces":
        SITE = 'https://horo.mail.ru/prediction/pisces/today/'
        bot.send_message(message.from_user.id, getHoroscope(SITE))
    else:
        bot.send_message(message.from_user.id, "Звезды не всемогущи, они не могут дать ответ на это(\n Напиши /help.")

def getHoroscope(SITE):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
    full_page = requests.get(SITE, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "article__item article__item_alignment_left article__item_html"})
    return convert[0].text

bot.polling(none_stop=True, interval=0)