import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

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

def get_points(win, loss, otloss):
    total_points = win + otloss*2


output = csv.writer(open('test2.csv', 'w')) # create output file
output.writerow(['Team Name', 'Record', 'Pts', 'Pts/game'])
d = {}
tbli = 0
while tbli < 4: # 4 divisions
    table = soup.findAll('table')[tbli] # select first table (Central Division)
    tbli+=1
    print('')
    output.writerow(' ')
    for i in table.select('tr'): # iterate through table
        col = i.select('td') 
        if col:
            team_name = col[0].text.strip()
            team_rec = col[5].text.strip()
            d.update({team_name:team_rec}) # add into dictionary pairs

            rec_split = team_rec.split('-') # calculate points
            rec_wins = int(rec_split[0])
            rec_loss = int(rec_split[1])
            rec_otloss = int(rec_split[2])
            get_points(rec_wins, rec_loss, rec_otloss)
            total_points = rec_wins + rec_otloss*2

            total_games_played = rec_wins + rec_loss + rec_otloss # calculate points/game
            ppg = str(round(total_points/total_games_played, 2))

            # output data
            output.writerow([team_name,team_rec, total_points, ppg]) # add to output csv
            print('{}:  {}'.format(team_name, team_rec))

            




# with open('test.csv', 'w') as fp:
#     writer = csv.writer(fp)
#     writer.writerow(['Team',' Record'])
#     for i in d.keys():
#        fp.write("%s, %s\n" % (i, d[i]))



