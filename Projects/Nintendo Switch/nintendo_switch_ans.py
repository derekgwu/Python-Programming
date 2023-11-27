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

"""Milestone 1: Game Installation"""
class QuizGame:
    def __init__(self, name):
        self.name = name
        return
    
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

"""Milestone 2: Making the Switch Work"""
