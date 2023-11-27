from nintendo_switch_ans import *
from nintendo_switch import *

#comment out the first line to test your code
"""STUDENT COPY"""


"""OWNER COPY"""

def milestone1():
    tests_pass = 0
    try:
        tests_pass += asserter(1.1, "switchuser357", user1.get_name(), False)
        tests_pass += asserter(1.2, [], user1.get_games(), False)
        tests_pass += asserter(1.3, "English", user1.get_language(), False)
        user1.set_language("Spanish")
        tests_pass += asserter(1.4, "Spanish", user1.get_language(), False)
    except: 
        tests_pass += asserter(1, 0, 0, True)
    
    if(tests_pass == 4):
        print("MILESTONE 1 COMPLETE!")
    else:
        print("MILESTONE 1 FAILED: " + str(tests_pass) + "/4 passed.")

def milestone2():
    tests_pass = 0
    

#The asserter
def asserter(test_case, exp, ret, exception):
    if(exception == True):
        print("Test Case " + str(test_case) + " had an exception")
        return 0
    if(exp == ret):
        print("Test Case " + str(test_case) + " SUCCESS!")
        return 1
    else:
        print("Test Case " + str(test_case) + " FAILED. We expected: " + str(exp) + " but you returned " + str(ret))
        return 0

user1 = User("fake_email@gmail.com", "password", "switchuser357")
milestone1()
quiz_game = QuizGame("quiz")
user1.add_game(quiz_game)
user1.select_game(0)