#!/usr/bin/bash

# Drake Wagner
# dbw2tn@virginia.edu

import sys
import os
import requests
from bs4 import BeautifulSoup
sys.tracebacklimit = 0

url = 'https://fatwreck.com/pages/tour-dates'
headers = {'user-agent' : 'dbw2tn@virginia.edu (Chrome/95.0.4638.69)'}

display_names = []
query_names = []
tour_dates = []
def get_dates(bands_list):
    global url, headers
    r = requests.get(url, headers = headers)
    print(r)
    src = r.content
    text = BeautifulSoup(src, 'html.parser')
    # tour_content = text.find('div', class_='fat-tour-dates-content')
    
    for band in text.find_all('div', id='band_info'):

        span1 = band.find('span', id='band_display_name')
        span2 = span1.findNext('span')

        display_names.append(span1.get_text())
        query_names.append(span2.get('id'))

    for band in text.find_all('div', id='tour_dates'):
        by_band = []
        dates = band.find_all('li', id='tour_date')
        for date in dates:
            dat = date.find('strong').get_text()
            loc = date.find('span', id='location').get_text()
            ven = date.find('span', id='venue').get_text()

            by_band.append([dat, loc, ven])
        tour_dates.append(by_band)
        # full.update({str(band):by_band}) # need band string name from last loop


# print(display_names)
# print(tour_dates)
# print(query_names)
get_dates()

full = dict(zip(display_names, tour_dates))

loop = 1
while loop == 1:
    state = input('State to check dates in: ').upper()
    print('Bands coming to {}:'.format(state))
    for band in display_names:
        for date in full.get(band):
            if str(state) in str(date):
                print(band, '...... ', date)
    cont = input('Check another? ')
    if cont not in ['yes', 'y', 'Yes']:
        loop = 0