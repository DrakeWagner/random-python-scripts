import requests
from bs4 import BeautifulSoup
import re

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

my_dict = dict()
# iterate through and collect stats
def stats_list(col_num, variable_name):
    mylist = []
    for i in stats[col_num::16]: #16 different columns
        mylist.append(i)
    my_dict[variable_name] = mylist

# send lists to select column names
# loop through colnames and add list to each?

# cols: ['', 'PLAYER', 'YRS', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'BB', 'SO', 'SB', 'CS', 'BA']

# for i in cols:
#     my_dict[i] = stats_list(cols.index(i)) # each group of stats printed in order

print(my_dict)

# iterate through and add keys to values
keys = ('', 'PLAYER', 'YRS', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'BB', 'SO', 'SB', 'CS', 'BA')
for i in range(0, 16):
    stats_list(i, keys[i])
print(my_dict)
