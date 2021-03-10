import requests
from bs4 import BeautifulSoup
import re
import requests

page = requests.get('https://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2020')
soup = BeautifulSoup(page.text, 'html.parser')

headers = soup.find_all('tr', attrs={'class' : 'colhead'})

body = soup.find('table', attrs={'class':'tablehead'})
# for i in body:
#     players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})#, attrs={'class':'oddrow player-10-33039'})
#     for i in players.find_all('td'):
#         print(i.get_text())
    
stats=[]
names=[]
# players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})
# for i in players:
#     stats_list=([y.get_text() for y in i.find_all('td')])
#     names.append((stats_list[1]))


# gets list of names on page
name_cell = soup.findAll(attrs={'class':re.compile('player-10-')})
for i in name_cell:
    name = i.find('span', attrs={'class':'bi'})
    if name is not None:
        names.append(name.text) 
print(names)

# get all stats from row
row = soup.find_all('tr', attrs={'class':re.compile('player-10-')})
for i in row:
    for stat in i.find_all('td'):
        stats.append(stat.get_text())


# take column names from table
cols = []
header = soup.find('tr', attrs={'class':'colhead'})
for i in header.find_all('td'):
    cols.append(i.get_text())


# iterate through and collect stats
def stats_list(col_num):
    for i in stats[col_num::16]: #16 different columns
        print(i)

print(stats_list(1))

# send lists to select column names
