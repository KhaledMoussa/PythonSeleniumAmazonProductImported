import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def search(search_term):

    asins = []

    for page in range(1, 2):

        template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1&page='
        search_term = search_term.replace(' ', '+')
        url1 = template.format(search_term)
        url = url1 + str(page)

        s = HTMLSession()
        r = s.get(url)
        r.html.render(sleep=1)
        items = r.html.find('div[data-asin]')

        for item in items:
            if item.attrs['data-asin'] != '':
                asins.append(item.attrs['data-asin'])

    asins = set(asins)

    print(len(asins), asins)

    filename = search_term

    df = pd.DataFrame(asins)
    df.to_csv('%s.csv' % filename, index=False, encoding='utf-8')
    return asins


search("dress")