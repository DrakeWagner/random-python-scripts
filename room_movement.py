# emulating room transitiong in text-based adventure games

import os
import sys
# import terms
# import items
# import commands

def main():
    pass
if __name__ == '__main__':
    main()


NORTH=0
EAST=1
SOUTH=2
WEST=3
UP=4
DOWN=5

rooms = {'kitchen': {
    'name':'kitchen', 
    'description':'You stand in the kitchen. It\'s a kitchen.',
    'items':['pan','pot'],
        'north':'living room', 
        'west':'bathroom', 
        'south':'entrance room'},
        'living room': {
    'name':'living room',
    'description':'null',
        'south': 'kitchen'},
        'bathroom': {
    'name':'bathroom', 
    'description':'null',
        'east': 'kitchen'},
        'entrance room': {
    'name':'entrance room', 
    'description':'null',
        'north':'kitchen'}}

# items when in inv and when in room
room_item_desc = {'pot':{'main_desc':'A pot is sitting on the shelf.',
                        'in_room':'A shiny pot sitting on the shelf.',
                         'in_inv':'It still has some water in it.'},
                  'pan':{'main_desc':'a pan is on the stove.',
                         'in_room':'A large pan sitting on the stove.',
                         'in_inv':'There is a slice of bacon sitting in it. Yum!'}}
# inv_item_desc = {'pot':'It still has some water in it',
#                  'pan':'There is a slice of bacon sitting in it. Yum!'}
    
dirs = {'n':NORTH, 'N':NORTH, 'north':NORTH, 'North':NORTH,
        'e':EAST, 'E':EAST, 'east':EAST, 'East':EAST,
        's':SOUTH, 'S':SOUTH, 'south':SOUTH, 'South':SOUTH,
        'w':WEST, 'W':WEST, 'west':WEST, 'West':WEST, 'weast':WEST,
        'up':UP, 'Up':UP, 'u':UP, 
        'down':DOWN, 'Down':DOWN, 'd':DOWN}

# Starting stats        
current_room = rooms['kitchen']
inventory = []


def move(direction):
    global current_room
    print(current_room['name'])
    global dirs
    if direction in dirs:
        if direction in current_room:
            current_room = rooms[current_room[direction]]
            print('You move ', direction, ' into the ', current_room['name'], sep='')
        elif direction not in current_room:
            print('cannot go {}'.format(direction))
        else:
            print('error')
    elif direction not in dirs:
        print('%s is not a valid direction.' % direction)
    else:
        print('nope')

def inspect(item):
    global current_room
    if item in current_room['items']:
        print(room_item_desc[item]['in_room'])
    elif item in inventory:
        print(room_item_desc[item]['in_inv'])
    else:
        print('not found')

def take(item):
    if item not in current_room['items']:
        print('item not found!')
    elif item in inventory:
        print('You already have that item')
    elif item in current_room['items']:
        print('You take the %s.' % item)
        inventory.append(item)
        current_room['items'].remove(item)
    
def my_inventory():
    global inventory
    if len(inventory) > 0:
        print('||| Inventory |||')
        for item in inventory:
            # keep syntax at end of line, regardless of length of item word?
            print('||| ', item, ' ', sep='')
        print('')
    elif len(inventory) == 0:
        print('Inventory empty.')

def north():
    move('north')

def east():
    move('east')

def south():
    move('south')

def west():
    move('west')

def help():
    print('valid commands:\n- move [direction]\n- look\n')

def search():
    # Room and item descriptions
    print(current_room['description'], end=' ')
    # remove item descriptions in room once item is taken
    # list of each item description, only print description of items present in current_room['items']?
    for item in room_item_desc:
        if item in current_room['items']:
            print(room_item_desc[item]['main_desc'], sep=' ', end=' ')

def exit():
    pass

# command prompt
while True:
    command = input('\nWhat will you do? ').lower()
    command_list = command.split()
    if any(x in ['move','go'] for x in command_list):
        if any(item in dirs for item in command_list):
            move(command_list[1])
        elif not any(item in dirs for item in command_list):
            print('Invalid command. Try \"move [direction]\"')
    elif any(x in command_list for x in ['look', 'inspect', 'investigate', 'examine', 'check']):
        # if command == 'look':
        #     print('look where? ', end='')
        # elif command != 'look':
        #     print(command, 'what? ', end='')
        # inspected_item = input('')
        # if inspected item in list of possible items in current room
        possible_inspect_item_room = list(set(current_room['items']).intersection(command_list))
        possible_inspect_item_inv = list(set(inventory).intersection(command_list))
        if len(possible_inspect_item_room) > 0:
            inspect(possible_inspect_item_room[0])
        elif len(possible_inspect_item_inv) > 0:
            inspect(possible_inspect_item_inv[0])
        else:
            print('error: inspect')
            # Rewrite to say list item to inspect?
            # input to add item to command?
    elif 'inventory' in command_list:
        my_inventory()
    elif command in ['help']:
        help()
    elif command in ['exit', 'quit', 'end']:
        exit()
    elif command == 'inventory':
        print(inventory)
    elif command == 'search':
        search()
    elif 'take' in command_list:
        '''
        possible items = any items in the command that are also in current room
        if any items in current room are also in command:
            take, and take only first if more than one in command
            (add to inv remove from room)
        if item in inventory:
        '''
        possible_items = list(set(current_room['items']).intersection(command_list))
        if any(x in current_room['items'] for x in command_list):
            if len(possible_items) > 1:
                print('taking first mentioned item applicable...')
            take(possible_items[0])
        # else if command is in possible item list AND already in inventory
        elif any(x in inventory for x in command_list):
            print('You already have that item!')
        else:
            print('I don\'t know what that is.')
    else:
        print('invalid command')



# while True:
#     print('current location: {}'.format(current_room['name']))
#     command = input('Which direction? ')
#     if command in dirs:
#         if command in current_room:
#             current_room = rooms[current_room[command]] # switch current room
#         else:
#             print('cannot move that direction')

