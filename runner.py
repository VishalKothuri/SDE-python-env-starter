#Archive
'''
player_row = 0
player_column = 0

print("Directions:  (North (n), South (s), West (w) and East (e))")
print("Type quit when done")

keeper = input("Where do you want to move your character?: ")

while keeper != "quit":
    if keeper == "n":
        player_row = player_row - 1
    elif keeper == "s":
        player_row = player_row + 1
    elif keeper == "w":
        player_column = player_column - 1
    elif keeper == "e":
        player_column = player_column + 1
    keeper = input("Where do you want to move your character?: ")
    print(keeper)
    print(player_row)
    print(player_column)

print(player_row)
print(player_column)

player_row = 0
player_column = 0
'''
import random

def playerRunner(player_row,player_column,direction):
    new_row = player_row
    new_column = player_column
    if direction == "n":
        new_row = new_row - 1
    elif direction == "s":
        new_row = new_row + 1
    elif direction == "w":
        new_column = new_column - 1
    elif direction == "e":
        new_column = new_column + 1
    else:
        print("invalid direction")

    if room[new_row][new_column] == 'x':
        print("Its a wall")
        return(player_row,player_column)
    else:
        return(new_row,new_column)

def announce_walls(room_row, room_column):
  if room[room_row - 1][room_column] == 'x': 
    print('There is a wall up')
  if room[room_row + 1][room_column] == 'x': 
    print('There is a wall down')
  if room[room_row ][room_column - 1] == 'x': 
    print('There is a wall left')
  if room[room_row][room_column+ 1] == 'x': 
    print('There is a wall right')

def puzzle():
    randomWords = ["EXCELLENCE", "HONESTY", "TRUSTWORTHY", "LOYALTY"]
    correctPassword = random.choice(randomWords)

    print("You see these words around the room:")
    for word in randomWords:
        if correctPassword == word:
            print(word.lower())
        else:
            print(word)

    password = input("What is the password? ")

    while password.lower() != correctPassword.lower():
        print("Access Denied!")
        print("Watch the words closely!")
        password = input("Try again: ")

def doorPuzzle():
    print(f"Welcome to our escape room, {name}")

    doorChoice = input("Choose a door from 1-3: ")

    while doorChoice != "3":
        if doorChoice == "1":
            print("You died by a room full of venomous snakes!")
            doorChoice = input("Try again: ")
        elif doorChoice == "2":
            print("You died by a hungry tiger!")
            doorChoice = input("Try again: ")
        else:
            print("Pick a number between 1-3!")
            doorChoice = input("Try again: ")
    print("You picked the right one!")

room = [
    'xxxxxxxx',
    'xx....px',
    'x....pex',
    'xx..d.px',
    'xxxxxxxx',
]

print("Directions:  (North (n), South (s), West (w) and East (e))")

room_row = 2
room_column = 1
hunger = 10

while room[room_row][room_column] != 'e':
    while hunger != 0:
        print(room_row,room_column)
        announce_walls(room_row,room_column)
        keeper = input("Where direction do you want to move your character?: ")
        room_row,room_column = playerRunner(room_row,room_column,keeper)

        if room[room_row][room_column] == 'p':
            puzzle()
            print("Move forward to your exit!")
        elif room[room_row][room_column] == 'd':
            doorPuzzle()
            print("Yay you survived! Keep moviing to find the exit!")
        hunger = hunger - 1

if hunger == 0:
    print("You lose!")

if room[room_row][room_column] == 'e':
    print("Yay you did it!")