# scrape for weather?
# bash "weather report" for "is it cold? y/n", etc.
# 7 day forcast?
# type in location to console to search?
# Update: Accuweather does not allow scraping

import requests
import csv
from bs4 import BeautifulSoup
import datetime

URL = 'https://www.accuweather.com/en/us/harrisonburg/22802/daily-weather-forecast/336229'
result = requests.get(URL)
print(result.status_code)
src = result.content # store page content as variable
soup = BeautifulSoup(src, 'html.parser') # parse/process source, to allow access
# of certain information
print(soup.title) # title