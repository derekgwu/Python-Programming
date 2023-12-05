from nintendo_switchans import *
from nintendo_switch import *
while(True):
    if logged_in == False:
        in_stream = input("""Enter L to log into an existing user or C to create a new user: """)
        if in_stream == "L" and len(users) == 0:
            print("There are no users")
            continue
        elif in_stream == "L":
            current_user = getValidUser()
            logged_in = True
            continue
        elif in_stream == "C":
            createUser()
            continue
        else:
            print("Please enter a valid input")
            continue


    #else user must be logged in
    print("Welcome " + current_user.get_name() + "! Press P to play a game, I to install game, L to log out")
    in_stream = input()
    if in_stream == "L":
        logged_in = False
        continue
    if in_stream == "P":
        game = current_user.select_game(0)
        game.play()
    if in_stream == "I":
        open_eshop()
