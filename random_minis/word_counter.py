a = 'a pig walked into a bar. He sat down and took off his hat.'
a_with_punct = a.split()# separates by spaces

# omits = '\"!,.:;\'?'
# for char in omits:
#     a_omitted = a.replace(char,'')
a_omitted = a.replace('.', '')
a_without_punct = a_omitted.split() 


def word_count(sentence):
    words = len(sentence)
    print('Number of words: ', words)

print(a_without_punct)
print(a_with_punct)

word_count(a_without_punct)



def check_for_word():
    word_search = input('Enter a word you would like to check for: ')
    if word_search in a_without_punct:
        times = a_without_punct.count(word_search)
        print('This word occurs ', times, ' time(s).', sep='')
    elif word_search not in a_without_punct:
        print('This word is not in the list')

check_for_word()
