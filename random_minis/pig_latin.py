'''
Takes an input and converts it into pig latin lol
'''

sentence = input('Input: ')

list = sentence.lower().split(' ')
new_list = []
for i in list:
    if i[0] in 'aeiou':# first
        new_list.append(i + 'way')
    elif i[0] not in 'aeiou':
        
        new_list.append(i + 'ay')
    
    i[-1] # last
    
print(' '.join(new_list))