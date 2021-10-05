# Ghost Game
from random import randint
print('Ghost Game')
feeling_brave = True
score = 0

while feeling_brave:
    ghost_door = 2
    print('Three doors ahead...')
    print('A ghost is behing one...')
    print('Which door do you open?')
    door_num = input('1, 2, 3')
    if door_num == ghost_door:
        print('GHOST!')
        feeling_brave = False
    else:
        print('There was not a ghost.')
        print('You enter the next room...')
        score = score+1
print('RUN AWAY!')
print('Game Over! You scored: ', score)