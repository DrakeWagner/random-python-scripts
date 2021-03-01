import requests
import csv
from bs4 import BeautifulSoup

URL = 'https://www.oddsshark.com/nhl/standings'
result = requests.get(URL)

print(result.status_code) # Check for 200 response
# print(result.headers)

src = result.content # store page content as variable
soup = BeautifulSoup(src, 'html.parser') # parse/process source, to allow access
# of certain information
print(soup.title) # title

# links=soup.find_all("a")
# for i in links:   # select links with Tampa in it
#     if "Tampa" in i.text:
#         print(i)

links = []
for i in links:
    links.append(i.get('href')) # URLs

table=soup.find_all('table')
a = table[0]
b = a.find_all('td')[4]
print(b)

table = soup.findAll('table')[0] # select first table (Central Division)
# for tr in table.findAll('tr'): # all rows
#     for td in tr.findAll('td'): # all cells of row
#         print(td)

tbli = 0
while tbli < 4:
    table = soup.findAll('table')[tbli] # select first table (Central Division)
    tbli+=1
    print('')
    for i in table.select('tr'): # iterate through table
        col = i.select('td') 
        if col:
            team_name = col[0].text.strip()
            team_rec = col[5].text.strip()
            print('{}:  {}'.format(team_name, team_rec))
