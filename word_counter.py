a = 'a pig walked into a bar. He sat down and took off his hat.'

def word_count(sentence):
    words = len(sentence.split())
    print('Number of words: ', words)

word_count(a)

def check_for_word():
    word_search = input('Enter a word you would like to check for: ')
    if word_search in a:
        times = a.count(word_search)
        print('This word occurs ', times, ' times.', sep='')
    elif word_search not in a:
        print('This word is not in the list')

check_for_word()