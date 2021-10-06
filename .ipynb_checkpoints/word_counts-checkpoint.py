# Drake Wagner
# dbw2tn

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.readinglength.com/book/isbn-{}'
ISBN = [base_url.format('0062225677'), base_url.format('0062225685')]
ISBN_TEST = [base_url.format('055131075')] 


discworlds_read = ['0062225677', '0062225685', '0552131059', '0552131067', '0062225723', '0062225731']
sk_read = ['1501182099', '0345806794', '0385199570', '1982110589', '0345806786', 
           '1501143689', '0307743667', '1789096499', '1501143859', '1501144529', 
           '1501144200', '1789091551']
sanderson_read = ['d0765326353', '0765365286', '0765360039', '1250166543']
book_names = []
book_lens = []
valid_isbn_list = []

# add and check if word count is zero, too
def CheckISBN(isbn_list):
    for i in isbn_list:
        while True:
            global base_url
            linky = base_url.format(i)
            page = requests.get(linky)
            src = page.content
            soup = BeautifulSoup(src, 'html.parser')
            text = soup.find_all(text=True)
            if 'The ISBN given does not appear to be valid' in str(text):
                print('invalid isbn:', i)
                while True:
                    new_isbn = input('enter replacement isbn: ')
                    try:
                        len(new_isbn) == 10
                        new_isbn = int(new_isbn)
                        break
                    except:
                        print('Not a valid ISBN format. Try again (no dashes, 10 digits).')
                print('ISBN corrected to: {}'.format(new_isbn))
                valid_isbn_list.append(new_isbn)
                break
            else:
                print('valid isbn: ', i)
                valid_isbn_list.append(i)
                break





def Information(c): # c must stay as list, even if just one element
    for isbn_num in c:
        global base_url
        linky = base_url.format(isbn_num)
        page = requests.get(linky)
    #   print(page.status_code) # Check for 200 response
        src = page.content
        soup = BeautifulSoup(src, 'html.parser')
        text = soup.find_all(text=True)
        set([t.parent.name for t in text])

        while 'The ISBN given does not appear to be valid' in str(text):
                print('invalid isbn:', isbn_num)
                new_isbn = input('enter replacement isbn: ')
                if len(new_isbn) == 10:
                    isbn_num = new_isbn
                    print('ISBN corrected to: {}... Checking isbn...'.format(new_isbn))
                    soup = BeautifulSoup((requests.get(base_url.format(isbn_num))).content, 'html.parser')
                    text = soup.find_all(text=True)
                    set([t.parent.name for t in text])
                else:
                        print('Not a valid ISBN format. Try again (no dashes, 10 digits).')
                valid_isbn_list.append(new_isbn)

        blacklist = [
            'b',
            'a',
            'script',
            'label',
            '[document]',
            'button',
            'h3',
            'style',
            'em',
        ]

        output=''
        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)

        [int(s) for s in output.split() if s.isdigit()]
        book_title = str(soup.find("h1"))

        book_title = book_title.replace("<h1>", "") 

        # remove h1 tags
        for ch in ['<h1>','</h1>']:
            if ch in book_title:
                book_title = book_title.replace(ch,'')
        book_title

        # 4th p tag is length
        length = str(soup.find_all("p")[4])
        for ch in ['<p>','<!-- --> words</p>',',']:
            if ch in length:
                length = length.replace(ch,'')
        length = int(length)
        print('\n')
        print('Title: {}\nLength: {}'.format(book_title, length))
        book_names.append(book_title)
        book_lens.append(length)
    print('\n==========')
    print(list(zip(book_names, book_lens)))
    print('Total words: {:,}'.format(sum(book_lens)))
    print('==========\n')


    
    
    
    
#Information(ISBN_nums)
# print(book_names)
# print(book_lens)
# print('Total words: {:,}'.format(sum(book_lens)))

Information(sanderson_read)
# CheckISBN(sanderson_read)
# print(valid_isbn_list)

'''
SK length: 1,826,635
Sanderson length: 1,087,645
'''