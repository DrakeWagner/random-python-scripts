import os
import pandas as pd
import numpy as np
from collections import Counter

cwd = os.getcwd()
print("PWD: {0}".format(cwd))

special_chars = '~`!@#$%^&*()-_=+[]{}|;:\'\",<.>/\\?'
with open('moby_dick.txt', 'r', encoding="utf8") as f:
    lines = f.read().lower().replace('\n', ' ').replace('.', '').replace(',', '') \
        .replace('!', '').replace('?', '').replace(';', '').replace(';', '')
    
f.close()


moby = lines.split()

print(len(lines))
print(len(moby))
print(lines[:100],\
moby[:20])

# Moust common words
f'Counter(moby).most_common(50)[45]'

# average length
char_len = 0
for i in moby:
    char_len += len(i)
avg_len = "%.2f" % (char_len / len(moby))
f'Average word length: {avg_len}'


print('******* Most used words *******')
print(Counter(moby))


word = input('Which word? ')
while True:
    index=0
    for i in moby:
        if i == word:
            index+=1
        elif i != word:
            pass
        elif i > len(moby):
            break
        else:
            print('error')
    print('Word occured {} times.'.format(index))
    break






# # dataframe
# moby = pd.DataFrame(lines)
# print(moby.head())


