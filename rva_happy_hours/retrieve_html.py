#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup
import time
from values import days, neighborhoods, cuisines

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

def define_url(day='Monday', neighborhood=None, cuisine=None):
    day = days.get(day)
    url = 'https://www.rvahappyhours.com/specials' + f'?day={day}'
    if neighborhood is not None:
        neighborhood = neighborhoods.get(neighborhood)
        url = url + f'&neighborhood={neighborhood}'
    if cuisine is not None:
        cuisine = cuisines.get(cuisine)
        url = url + f'&cuisine={cuisine}'
    return url

def retrieve_page(URL):
    page = requests.get(URL)
    cont = BeautifulSoup(page.content, "html.parser")

    # retrieve day for filename
    dayval = int(URL.split('day=')[1][0])
    daykey = list(days.keys())[list(days.values()).index(dayval)]

    text_file = open(f'rva_hr_{daykey}', "w", encoding="utf-8")
    text_file.write(str(cont))
    text_file.close()
    
    return cont

def main():
    path = os.getcwd() + r'/hr_html'
    os.mkdir(path)
    os.chdir(path)

    for d in days:
        retrieve_page(define_url(d))
        time.sleep(.5) # just in case ;)

main()