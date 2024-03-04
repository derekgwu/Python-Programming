    
import time
import os
import random

#this generate a set of colors for the users to memorize
def generate_move(current_turn):
    bank = ["red", "blue", "green", "yellow"]
    order = []
    for i in range(0, current_turn):
        move = bank[random.randrange(0,4)]
        print(move)
        order.append(move)
        time.sleep(2)

        #develop a system to store the outputs (hint data structure!)

    #clears terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    return order

    #likely want to return the data structure

#your code here!
def play():
    #start on turn 1
    turn = 1
move = generate_move(3)
time.sleep(2)
print(move)

