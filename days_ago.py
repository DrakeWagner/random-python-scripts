# Checks how many days ago a date was
import datetime

date = input('Enter a date <MM-DD-YYYY>:  ')

m,d,y = date.split('-')
# dmy = (date.split('-'))
# month = int(dmy[0])
# day = int(dmy[1])
# year = int(dmy[2])
print(datetime.date(int(y),int(m),int(d)))
print(datetime.now())

# date2 = datetime.date(year, month, day)
# print(datetime.now() - date2)