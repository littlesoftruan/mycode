#!/usr/bin/python3
import random
import time
# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ', rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'north':'Bedroom',
        'item': ['key',"gun"]
    },

    'Kitchen': {
        'north': 'Hall',
        'item': ['monster'],
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'north west':'Bedroom',
        'item': ['potion'],
        'north': 'Pantry',
    },
    'Garden': {
        'north': 'Dining Room'
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': ['cookie'],
    },
    'Bedroom':{
        'south':'Hall',
        'east':'Pantry',
        'south east':'Dining Room',
        'west':'Library',
        'item':['pack of gold']
    },
    'Library':{
        'east':'Bedroom'
    },
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            rooms[currentRoom]['item'].remove(move[1])

        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
    elif currentRoom == 'Library' and "key" in inventory and 'pack of gold' in inventory:
        print('This is your second way to win the game. :)')
        break
    elif currentRoom == 'Library' and "key" not in inventory and 'pack of gold' not in inventory:
        print("Good, you hit a teleport point.")
        time.sleep(3)
        currentRoom = random.choice(list(rooms.keys()))

    ## If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print("You still have 50% chance to be survived")
        print("There is a dice is running background,let's see in 5 sec")
        time.sleep(5)
        if random.randint(1,6) <=3:
            print("lmao,Gamer Overrrrrrrrr!")
            break
        elif random.randint(1,6) >3:
            print("Congras,you still alive")
