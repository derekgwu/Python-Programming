#DESIGN YOUR OWN TEST/GAME SHOW

#you do not need to organize your problems into functions like I have
#however, please maintain proper indentation and proper variable naming types

#you may not use the assert keyword like I did. you must use if and else statements

def problem_1():
    #display the question
    print("Which of these is not a coding language? \n")

    #display the answer choices
    #be sure to use \n to create a new line the terminal
    print("A: C \n") 
    print("B: C++ \n")
    print("C: C+ \n")
    print("D: C# \n")

    #display and store user's variable
    user_ans = input("Enter in the corresponding letter:")
    assert user_ans == "C"

def problem_2():
    #display the question
    print("\nQuestion 2")
    print("True or False: Python is the oldest coding language \n")

    #display the answer choices
    print("True \n")
    print("False \n")

    #add a note that the user must enter T or F
    print("Please put T for True or F for false \n")

    user_ans = input("Enter in the corresponding letter: \n")
    assert user_ans == "F"
    
def problem_3():
    #display the question
    print("Question 3 \n")
    print("____ is the coding language I wrote this program in")

    #take user input
    user_ans = input("Enter your answer here: ")
    assert user_ans == "Python"

problem_1()
problem_2()
problem_3()
