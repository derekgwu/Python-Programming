"""Milestone 0: User Creation"""
#introduction to classes
class User:
    def __init__(self, email, password, username):
        self.name = username;
        self.password = password;
        self.games = []
        self.language = "English"

    def get_name(this):
        return this.name;

    def get_games(this):
        return this.games;

    def set_name(this, new_name):
        this.name = new_name

    def set_language(this, language):
        this.language = language

    def get_language(this):
        return this.language
    
    def add_game(this, game):
        this.games.append(game)
    
    def select_game(this, game_num):
        this.games[game_num].play()

"""Milestone 1: Game Installation and E-Shop"""
class QuizGame:
    def __init__(self, name):
        self.name = name
        return
    
    def get_name(this):
        return this.name
    
    def play(this):
        print('Welcome to AskPython Quiz')
        answer=input('Are you ready to play the Quiz ? (yes/no) :')
        score=0
        total_questions=3

        if answer.lower()=='yes':
            answer=input('Question 1: What is your Favourite programming language?')
            if answer.lower()=='python':
                score += 1
                print('correct')
            else:
                print('Wrong Answer :(')


            answer=input('Question 2: Do you follow any author on AskPython? ')
            if answer.lower()=='yes':
                score += 1
                print('correct')
            else:
                print('Wrong Answer :(')

            answer=input('Question 3: What is the name of your favourite website for learning Python?')
            if answer.lower()=='askpython':
                score += 1
                print('correct')
            else:
                print('Wrong Answer :(')

        print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
        mark=(score/total_questions)*100
        print('Marks obtained:',mark)
        print('BYE!')
eshop = []
game1 = QuizGame("Quiz Game")
eshop.append(game1)


"""Milestone 2: Making the Switch Work"""
logged_in = False
users = []
current_user = 0

def getValidUser():
    for i in range(0, len(users), 1):
        print("[" + str(i) + "] " + users[i].get_name())
    in_stream = input("Enter the number of the user you want to pick: ")
    return users[int(in_stream)]

def createUser():
    new_user = User(input("Enter email: "), input("Enter password: "), input("Enter username: "))
    users.append(new_user)
    return new_user

def open_eshop():
    for i in range(0, len(eshop), 1):
        print("[" + str(i) + "] " + eshop[i].get_name())
    in_stream = input("Enter the number of the game you want to install: ")
    current_user.add_game(eshop[int(in_stream)])
    print(eshop[int(in_stream)].get_name() + " installed")
    

    



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
