#Practice 2 - Debugging
#This week we will get practice finding bugs in our code and fixing them
#For each example, identify the bug(s) and fix them.

"""Given a number, the function checkpoint() checks if the number is greater than 1, 3, 5, 7, and 9.
If the number is greater than one number, it will add 1 to the checkpoint counter. At the end, it returns
the number of checkpoints"""
#num: 8
def checkpoint(num):
    checkpoints_passed = 0;
    if(num > 1):
        checkpoints_passed += 1
    if(num > 3):
        checkpoints_passed += 1
    if(num > 5):
        checkpoints_passed += 1
    if(num < 7):
        checkpoints_passed += 1
    if(num > 9):
        checkpoints_passed += 1
        
    return checkpoints_passed

"""Given a string, the function seasonal() checks if the string represents a season of the year. Returns true if it does,
or false if it is not a season in the year"""
def seasonal(name):
    if(name == "fall"):
        return True
    elif(name == "spring"):
        return True
    elif(name == "winter"):
        return True
    elif(name == "summer"):
        return True
    
    return False

"""Given a number, the function is_negative() checks if the value is negative or not. Returns true if it does, or false 
if its not"""
def is_negative(num):
    if(num < 1):
        return False
    
    return True


#HARD try for extra credit!
"""Given a number, the function div_3_and_2() checks if the number can be divided by 2 AND 3. Returns True if it does, or
false if it not divisible by 3 or 2"""
def div_3_and_2(num):
    if(num % 3 == 0 & num % 2 == 0):
        return True
    return False





###TEST CASES DO NOT ALTER PAST HERE
def test(assertion, expected, test_num):
    if(assertion == expected):
        print("Test " + str(test_num) + ": SUCCESS.")
    else:
        print("Test " + str(test_num) + ": FAILED. Expected " + str(expected) + " but got " + str(assertion))

#This will test all of the methods at once
test(checkpoint(10), 5, 1.1)
test(checkpoint(3), 1, 1.2)
test(checkpoint(0), 0, 1.3)
test(seasonal("summer"), True, 2.1)
test(seasonal("pizza"), False, 2.2)
test(seasonal("autumn"), True, 2.3)
test(is_negative(-100), True, 3.1)
test(is_negative(0), False, 3.2)
test(is_negative(1), False, 3.3)
test(div_3_and_2(6), True, 4.1)
test(div_3_and_2(10), False, 4.2)
test(div_3_and_2(0), True, 4.3)
