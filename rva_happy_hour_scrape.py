#!/usr/bin/env python3

import sys
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
sys.tracebacklimit = 0


days = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday':5, 'Saturday': 6, 'Sunday': 7}
neighborhoods = {'Brandermill-Woodlake': '1b90bbff-2847-4e44-a6f9-dcf5ba26cf02',
    'Church Hill-Rockett\'s Landing': '7cdd399e-9b65-4261-89c1-3c883c768ad1',
    'Downtown-Jackson Ward': '290653de-4577-4699-beb1-fbd462e77533',
    'East End': '1e9fd0ab-9452-4175-8f94-8913a076b158',
    'Glen Allen-Wyndham': '3e80d5a0-c460-4c8d-b1b3-d72ab91f9ebd',
    'Manchester-Forest Hill-Stratford Hills': 'cbe0e9a2-671b-477a-b4e1-513347d2ca0a',
    'Midlothian-Bon Air': 'a722bf6a-3b60-428b-bc52-7331a52ae905',
    'Museum District': 'a47d2d13-9f5d-491a-80a1-2b27e75a2d9d',
    'Near West End': 'f92edbe9-abcc-47c0-b4a3-64579745cfd6',
    'North Chesterfield-South Richmond': '78cf86a0-6671-4b1c-b1e1-4b4f13ead8d4',
    'North Side': '7b42b74b-0aea-4926-ac7e-b524853e35c6',
    'Scott\'s Addition': '314271cb-b815-483b-8afd-ac793e2968e7',
    'Shockoe Bottom/Slip': 'c432c343-96d5-4d61-aecd-57f8e36e8935',
    'Short Pump-Innsbrook': '7227c4de-16ab-420f-913e-401521ebcac2',
    'The Fan': '235281ee-d22f-41bd-9874-9d150af11230',
    'West End': 'cd6f2524-1537-4688-b469-3c3ffe8dfdb6'}
cuisines = {'American':'40acd385-1505-4845-b374-aefbbe9ea642',
    'American (New)':'30ea0330-4a5c-4e8e-9ed4-83540439ae2e',
    'Asian (Other)':'98d85713-c323-47cd-aec6-7540c4095906',
    'Barbecue':'0fb93f75-c116-43f9-8d31-82721acfeecf',
    'Brewery/Wine Bar/Distillery':'7133d159-8b04-43f8-ab5c-046939472755',
    'Burgers':'5a31ff2a-0416-463b-8c5f-3ca9c28881d0',
    'Cafe/Diner':'98a005d4-60bf-4b4d-a922-a028bdf7302b',
    'Chinese':'3d1a89d7-eeb8-4fe7-9037-0318e87193b7',
    'Cuban':'decb5b72-ea34-4f4f-9251-e92e190621d3',
    'Dessert':'b8d33675-9b59-4614-9ece-b538b562c3f0',
    'European (Other)':'d71df770-67ba-4dba-8669-b8c6e4517d96',
    'Irish':'d5edc60c-9be6-4fa0-8ad3-b5a934021aeb',
    'Italian':'6f718411-4533-48cd-bd8b-8e2ffa8b79cf',
    'Japanese':'6822f679-ab1b-4991-928e-b7be3548167a',
    'Korean':'c6d86af1-68bc-47c5-a06d-a918d40f4c00',
    'Mediterranean':'4808469f-4a75-41cf-9410-fbefc4a1e513',
    'Mexican/Latin-American':'1c7e1629-bc43-4796-9ca5-efafd401a240',
    'Pizza':'5c715256-eb01-4931-be0a-7866042572e8',
    'Seafood':'fc7b7b42-9fa4-4e48-b5df-5fd9342ed170',
    'Southern':'a89c9446-6bea-4211-a224-02045d765926',
    'Steakhouse':'4c4b979d-cde4-476b-97e0-a7ea8d5949c9',
    'Thai':'0ee41ce4-619c-4c0d-8974-f20b7f33da52',
    'Vietnamese':'812c9a5f-5824-4307-8d4a-aa92d7734517'}

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

print(define_url('Wednesday', 'Scott\'s Addition'))


