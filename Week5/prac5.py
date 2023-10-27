"""UNIT TESTS!!!!!!"""
global children
children = []


def hour_one():
    tests_passed = 0;
    #tests that three new child have been created
    try:
        for child in children:
            if len(child[0]) <= 0:
                print("Test 1.1 Failed: No child detected")
            else:
                tests_passed += 1

            
            if child[1] != 0:
                print("Test 1.2 Failed: Child does not have 0 candies")
            else:
                tests_passed += 1
        
        if tests_passed == 6:
            print("Test Case 1.1: SUCCESS")
            print("Test Case 1.2: SUCCESS")
        else:
            print("Test Case 1.1 Failed: Not enough children")
            print("Test Case 1.2 Failed: Not enough children")
        children_prev = children.copy()
    except:
        print("Test Cases 1 Failed: Out of bounds exception")

def hour_two():
    val_six = 0
    val_eight = 0
    #tests whether the candy count for each child is correct
    try:
        for child in children:
            if child[1] == 6:
                val_six += 1
            if child[1] == 8:
                val_eight += 1
        if val_eight + val_six == 3:
            print("Test Case 2.1: SUCCESS")
        else:
            print("Test Case 2.2: Incorrect candy count values")
    except:
        print("Test Case 2.1: Out of Bounds Exception")

    #tests whether each child has jolly ranchers and snickers
    try:
        for child in children:
            if child[2] != "Jolly Ranchers" or child[3] != "Snickers":
                print("Test Case 2.2: Jolly Ranchers and Snickers not added")
                break
        print("Test Case 2.2: SUCCESS")
    except:
        print("Test Case 2.2: Out of Bounds Exception")
        
def hour_three():
    tests_passed = 0
    if len(children[3][0]) <= 0:
        print("Test Case 3.1: 4th child name not found")
    else:
        tests_passed += 1
    if children[3][1] != 8:
        print("Test Case 3.2: 4th child candy count is incorrect")
    else:
        tests_passed += 1
    test_pass = True
    for i in range(0,3,1):
        if children[i][1] != 10 and children[i][1] != 8:
            print("Test Case 3.3: Incorrect child candy counts")
            test_pass = False
            break
    if test_pass != False:
        tests_passed += 1

    if tests_passed == 3:
        print("Test Case 3.1: SUCCESS")
        print("Test Case 3.2: SUCCESS")
        print("Test Case 3.3: SUCCESS")
    
def hour_four():
    try:
        if children[2][1] != (4):
            print("Test Case 4:1: 3rd child has more candy than expected")
        else:
            print("Test Case 4.1: SUCCESS")
        if(children[0][1] != 14 and children[0][1] != 12):
            print("Test Case 4.2: 1st child does not have enough candy")
        else:
            print("Test Case 4.2: SUCCESS")
        
        if(len(children[2]) != 3):
            print("Test Case 4.3: 3rd child has extra candy type")
        else:
            print("Test Case 4.3: SUCCESS")
    except:
        print("Test Case 4.1: Out of bounds exception")
        print("Test Case 4.2: Out of bounds exception")
        print("Test Case 4.3: Out of bounds exception")

def hour_five():
    ans = [28,16,4,16]
    correct = True
    for i in range(0,4,1):
        if children[i][1] != ans[i]:
            correct = False
    if correct == False:
        print("Test Case 5.1: Incorrect candy count for at least one child")
    else:
        print("Test Case 5.1: SUCCESS")
    
    ans2 = [5,5,3,3]
    correct = True
    
    for i in range (0,4,1):
        if len(children[i]) != ans2[i]:
            correct = False
    if correct == False:
        print("Test Case 5.2: Incorrect candy types for at least one child")
    else:
        print("Test Case 5.2: SUCCESS")

def hour_six():
    found = False
    for x in children[1]:
        if x == "Snickers":
            print("Test Case 6.1: Snickers found in 2nd child")

    found = False
    for x in children[0]:
        if x == "Jolly Ranchers":
            print("Test Case 6.2: Jolly Ranchers found in 1st child")
            found = True
            
    if found == False:
        print("Test Case 6.2: SUCCESS")

    found = False
    for x in children[3]:
        if x == "Jolly Ranchers":
            print("Test Case 6.3: SUCCESS")
            found = True
    if found == False:
        print("Test Case 6.3: Could not find Jolly Ranchers in 4th child")

"""ASSIGNMENT STARTS HERE!"""
"""Refer to prac5directions.md to see what should happen at each hour"""

#3:00 PM
children.append(["John", 0])
children.append(["Harry", 0])
children.append(["Peter", 0])
"YOUR CODE HERE"

hour_one()
#4:00 PM

"YOUR CODE HERE"

hour_two()

#5:00 PM

"YOUR CODE HERE"

hour_three()


#6:00 PM

"YOUR CODE HERE"

hour_four()
#7:00 PM


"""YOUR CODE GOES HERE"""

hour_five()
#8:00 PM

"YOUR CODE HERE"


hour_six()
    







