"""Milestone 0: User Creation"""
#the class, User, represents a singular user on the switch
class User:
    """the constructor takes three Strings and sets an email, password, and username. It should
    also create an empty array of games and set the language to english""" 
    def __init__(self, email, password, username):
        0

    #gets the username of the user
    def get_name(this):
        0
    
    #gets the array of games
    def get_games(this):
        0
    
    #set an new username
    def set_name(this, new_name):
        0
    
    #sets a new language
    def set_language(this, language):
        0
    
    #gets the current language of the system
    def get_language(this):
        0
    
    #save for milestone 2

    #adds a new game to the array of games
    def add_game(this, game):
        0

    #plays a game from the user array list of game
    def select_game(this, game_num):
        0

"""Milestone 1: Game Installation and E-Shop"""
class QuizGame:
    def __init__(self, name):
        0
    
    def get_name(this):
        0

    def play(this):
        0


#The eshop, any new game you make should be added to the eshop
eshop = []



"""Milestone 2: Making the Switch Work"""
logged_in = False
users = []
current_user = 0

def getValidUser():
    0

def createUser():
    0

def open_eshop():
    0
    

    




#This runs the switch itself
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
