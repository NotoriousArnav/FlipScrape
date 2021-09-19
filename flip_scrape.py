#!/usr/bin/env python3
import requests as r
from bs4 import BeautifulSoup

class FlipkartProduct:
    def __init__(self, url):
        page = r.get(url)
        soup = BeautifulSoup(page.content, 'lxml')

        title = soup.find('h1', class_='yhB1nd')
        title_span = title.find('span')
        self.prod_name = title_span.text

        self.rating = soup.find('div', class_='_3LWZlK').text
        self.rNr = tuple([int(x) for x in soup.find('span',class_='_2_R_DZ').text.replace('\xa0', '').replace('Ratings','').replace('Reviews', '').replace(',', '').split('&')]) 
        curr_price = soup.find('div', class_='_30jeq3 _16Jk6d').text
        currency = curr_price[0]
        self.price = int(curr_price[1:].replace(',', ''))
        
        self.qna = [
                {'question':question.find('div',class_='_1xR0kG _3cziW5').find_all('span')[1].text,
                    'answer':question.find('div', class_='_2yeNfb').find_all('span')[1].text}
                for question in qna
        ]
        
        try:
            prev_price = soup.find('div', class_='_3I9_wc _2p6lqe').text
            self.prev_price_amnt = int(prev_price[1:].replace(',', ''))

            self.discount = {}
            self.discount['percent'] = int(soup.find('div', class_='_3Ay6Sb _31Dcoz').text.split('%')[0])
            self.discount['amount'] = self.prev_price_amnt - self.price
        except:
            self.prev_price_amnt = None
            self.discount = None

