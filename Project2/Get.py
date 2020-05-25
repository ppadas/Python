import requests
from bs4 import BeautifulSoup

SITE = 'https://horo.mail.ru/prediction/aries/today/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
full_page = requests.get(SITE, headers=headers)
soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("div", {"class": "article__item article__item_alignment_left article__item_html"})
print(convert[0].text)
