i=0
while i < 5:
    print(i)
    i += 1

class Soda():

    # class attribute (is assigned to all instances of Soda)
    latin = 'nitri'

    def __init__(self, color, flavor, sugar_contents):
        self.color = str(color)
        self.flavor = flavor
        self.sugar_contents = int(sugar_contents)

    def __str__(self):
        return 'This soda is {}, tastes like {}, and has {} \
grams of sugar.\n'.format(
            self.color, self.flavor, self.sugar_contents
        )

    # Instance method
    def color_description(self):
        return f'The {self.color} color bubbles with carbination'

    # Instance method
    def taste(self, sweetness):
        return f'{self.flavor} is {sweetness}/10 on a scale of sweetness.' # f-string
    

grape_soda = Soda('purple', 'grape', 42)
print(grape_soda)

class Diet(Soda):

    def __init__(self, color, flavor, sugar_contents=0):
        Soda.__init__(self, color, flavor, sugar_contents)

    def __str__(self):
        return 'This diet soda is {} and tastes like {}.\n'.format(
            self.color, self.flavor
        )

diet_coke = Diet('brown', 'cola')
print(diet_coke)

print ('\n\n\n')
print('String formatting!!')
name = 'Drake'
age = 23
cityBorn = 'Tampa'

# % formatting, str.formatting, and f-strings: 3 ways to format
print('My name is %s. I am %s and was born in %s.' % (name, age, cityBorn))
print('My name is {}. I am {} and was born in {}.'.format(name, age, cityBorn))
print(f'My name is {name}. I am {age} and was born in {cityBorn}.')

# printf is the most versatile. You can put functions in them, call the method
# directly

print(f'{age*3} is triple my age! Nice.')
print(f'My name lowercase is: {name.lower()}')