import unittest
from test_func import match
from test_func import getHoroscope
import requests
from bs4 import BeautifulSoup

class TestNames(unittest.TestCase):
    def get_universal_name(self, name):
        for i, j in match.items():
            if name in j:
                return i

    def test_twins(self):
        self.assertEqual(self.get_universal_name('близнецы'), 'gemini')
        self.assertEqual(self.get_universal_name('близнец'), 'gemini')
        self.assertEqual(self.get_universal_name('twins'), 'gemini')
        self.assertEqual(self.get_universal_name('gemini'), 'gemini')

    def test_virgo(self):
        self.assertEqual(self.get_universal_name('virgo'), 'virgo')
        self.assertEqual(self.get_universal_name('дева'), 'virgo')

class TestHoroscope(unittest.TestCase):
    def test_twins(self):
        SITE = 'https://horo.mail.ru/prediction/gemini/today/'
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
        full_page = requests.get(SITE, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("div", {"class": "article__item article__item_alignment_left article__item_html"})
        self.assertEqual(getHoroscope('gemini'), convert[0].text)

    

if __name__ == "__main__":
  unittest.main()