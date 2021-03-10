import requests
import csv
from bs4 import BeautifulSoup
import datetime

URL = 'https://www.oddsshark.com/mlb/power-rankings'
result = requests.get(URL)

print(result.status_code) # Check for 200 response
# print(result.headers)

src = result.content # store page content as variable
soup = BeautifulSoup(src, 'html.parser') # parse/process source, to allow access
# of certain information
print(soup.title) # title

output = csv.writer(open('test123.csv', 'w'))
output.writerow(['Team', 'Rank', 'Change'])

# table = soup.findAll('table')
# print(table[1])

# a = soup.find_all('div', attrs={'class':'content'})
row = soup.find_all('tr')
for i in row.find('td'):
    print(row.get_text())