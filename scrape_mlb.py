import requests
import csv
from bs4 import BeautifulSoup
import datetime

URL = 'https://www.espn.com/mlb/standings'
result = requests.get(URL)

print(result.status_code) # Check for 200 response
# print(result.headers)

src = result.content # store page content as variable
soup = BeautifulSoup(src, 'html.parser') # parse/process source, to allow access
# of certain information
print(soup.title) # title

today = datetime.datetime.now()
today = today.strftime('%m-%d-%y')
datetime.datetime.now().date().isoformat()

output = csv.writer(open('MLB_Standings_{}.csv'.format(today), 'w'))
output.writerow(['Team Name', 'Record', 'PCT'])

# table = soup.find_all("div", {"class":"stat-cell"})
table = soup.findAll('tr', attrs={"class" : "Table__Scroller"})
print(table)


# soup.find_all('tr', attrs = {'class': 'oddrow player-10-33039'})

