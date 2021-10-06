# # i=0
# # while i < 5:
# #     print(i)
# #     i += 1

# # class Soda():

# #     # class attribute (is assigned to all instances of Soda)
# #     latin = 'nitri'

# #     def __init__(self, color, flavor, sugar_contents):
# #         self.color = str(color)
# #         self.flavor = flavor
# #         self.sugar_contents = int(sugar_contents)

# #     def __str__(self):
# #         return 'This soda is {}, tastes like {}, and has {} \
# # grams of sugar.\n'.format(
# #             self.color, self.flavor, self.sugar_contents
# #         )

# #     # Instance method
# #     def color_description(self):
# #         return f'The {self.color} color bubbles with carbination'

# #     # Instance method
# #     def taste(self, sweetness):
# #         return f'{self.flavor} is {sweetness}/10 on a scale of sweetness.' # f-string
    

# # grape_soda = Soda('purple', 'grape', 42)
# # print(grape_soda)

# # class Diet(Soda):

# #     def __init__(self, color, flavor, sugar_contents=0):
# #         Soda.__init__(self, color, flavor, sugar_contents)

# #     def __str__(self):
# #         return 'This diet soda is {} and tastes like {}.\n'.format(
# #             self.color, self.flavor
# #         )

# # diet_coke = Diet('brown', 'cola')
# # print(diet_coke)

# # print ('\n\n\n')
# # print('String formatting!!')
# # name = 'Drake'
# # age = 23
# # cityBorn = 'Tampa'

# # # % formatting, str.formatting, and f-strings: 3 ways to format
# # print('My name is %s. I am %s and was born in %s.' % (name, age, cityBorn))
# # print('My name is {}. I am {} and was born in {}.'.format(name, age, cityBorn))
# # print(f'My name is {name}. I am {age} and was born in {cityBorn}.')

# # # printf is the most versatile. You can put functions in them, call the method
# # # directly

# # print(f'{age*3} is triple my age!')
# # print(f'My name lowercase is: {name.lower()}')

# ### TRY EXCEPT STATEMENTS

# # try:
# #     print(variable)
# # except:
# #     print('This exception will print since \'variable\' is not defined')
# # else:
# #     print('This statement will execute ONLY if there are no errors raised')
# # finally:
# #     print('This will always print, error or not')


# # import os
# # '''Uncomment one at a time to get results for every error type listed'''
# # try:
# #     open('missing_file') # try to open missing file for reading
# #     print(int(1/0)) # zero division error
# #     print(int(9999999*9e99999)) # general arithmetic error for overflow
# #     os.listdir(5) # general IO error (technically a IsADirectoryError)
# #     str(9)*str(9) # general type error
# #     print(int('1d')) # general value error
# #     LetsGoBuccaneers # general exception class error
    
# # except FileNotFoundError:
# #     print('The FileNotFound error message (1)')   
# # except ZeroDivisionError:
# #     print('The ZeroDivisionError (2)')
# # except ArithmeticError:
# #     print('The ArithmeticError (3)')
# # except IOError:
# #     print('The General IO Error (4)')
# # except TypeError:
# #     print('The General Type Error (5)')
# # except ValueError:
# #     print('The General Value Error (6)')
# # except Exception:
# #     print('The General Exception Class (7)')



# # import os
# # '''Uncomment one at a time to get results for every error type listed'''
# # try:
# #     print(int(1/0)) # zero division error
# #     print(int(9999999*9e99999)) # general arithmetic error for overflow  


# # except ArithmeticError:
# #     print('The ArithmeticError (3)')
# # except ZeroDivisionError:
# #     print('The ZeroDivisionError (2)')


# # variable = input('Enter vairable: ').lower()
# # variable = variable.lower()
# # if variable == 'olive' or variable == 'olive Tree':
# #     print('True')

# # answers = ['olive', 'olive', 'olive tree']
# # if variable in answers:
# #     print('True')


# # for i in range(0,5):
# #     print(i)

# # i = 0
# # while i < 5:
# #     print(i)
# #     i += 1
# #     # i = i + 1


# # answer = ['olive']
# # tries = 0
# # while tries < 3: # check which try it is
# #     response = input('Enter guess')
# #     if response == 'olive':
# #         print('correct!')
# #         break
# #     elif response != 'olive':
# #         if tries == 0:
# #             print('first')
# #             tries += 1
# #         elif tries == 1:
# #             print('second')
# #             tries += 1
# #         elif tries == 2:
# #             print('You lose')




# # import pandas as pd
# # import json
# # import requests
# # users = requests.get("https://jsonplaceholder.typicode.com/users")
# # users = json.loads(users.text)
# # print(users[5]['company']['catchPhrase'])
# # print(users[9]['address']['geo']['lng'])

# class ACCOUNT:
 
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
 
 
 
#     def __str__(self): 
      
#         return "Account Number: "+str(self.account_number) +\
#                "Balance: " + str(self.balance)
                
 
    
# class CHECKING(ACCOUNT):
    
#     def __init__(self, account_number, balance, fee:float):
#         ACCOUNT.__init__(self, account_number, balance)
#         self.fee = fee
        
#     def __str__(self):
#         return "Acount Type: Checking" + \
#                "Account Number: " + str(self.account_number) + \
#                "Balance: " + str(self.balance)
        
#     def getFee(self):
#         self.fee = 3
#         return self.fee
        
        
#     def deposit(self, amount:int):
#         self.balance += amount
        
        
        
#     def withdraw(self, amount:int):
#         if self.balance - amount - self.fee < 0:
#             return "Insufficient Funds"
#         else:
#             self.balance = self.balance - (amount + self.fee)
#             return "Your new balance is: " + str(self.balance)
            
            
# check1 = CHECKING("1234", 500, .5)
# print(check1)
# check1.getFee()

# check1.withdraw(100)
# print(check1)

# check1.deposit(200)
# print(check1)
#Question 7
import requests
from bs4 import BeautifulSoup

website = "https://www.nytimes.com/"

result = requests.get(website)
print(result)