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

links=soup.find_all("a")
for i in links:   # select links with Tampa in it
    if "Tampa" in i.text:
        print(i)

for i in links:
    print(i.get('href')) # URLs

table=soup.find_all('table')
a = table[0]
b = a.find_all('td')[4]
print(b)

table = soup.findAll('table')[0] # select first table (Central Division)
for tr in table.findAll('tr'): # all rows
    for td in tr.findAll('td'): # all cells of row
        print(td)










# soup = BeautifulSoup(page.content, 'html.parser')

# print([type(item) for item in list(soup.children)]) # element types
# html = list(soup.children)[1]

# soup.find_all('p')[0].get_text()
# soup.findall('table table--')
