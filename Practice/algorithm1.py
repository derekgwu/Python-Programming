#given an array, identify all the even numbers and sum them together. return the sum
def sum_even(arr):
    return 0

#given an array, sum every third number in the array
def sum_three(arr):
    return 0

#given an array, find two numbers that add up to 10. you may assume there is only combination
def find_ten(arr):
    return 0

#given two arrays, construct a new array that only has numbers less than five
def less_than_five(arr1, arr2):
    return 0

#given a string and character, determine whether the character is in the strng. return either true or false
def letter_in_word(char, str):
    return 0


"""`````````````UNIT TESTS````````````````````"""

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

try:
    asserter(1.1, 4, sum_even([1,2,2]), False)
    asserter(1.2, 0, sum_even([1,3,5]), False)
    asserter(1.3, 12, sum_even([4,4,4]), False)
except:
    asserter(1, 0, [], 1, True)

try:
    asserter(2.1, 9, sum_three([1,2,3,4,5,6]), False)
    asserter(2.2, 3, sum_three([1,2,3]), False)
    asserter(2.2, 0, sum_three([1,2]), False)
except:
    asserter(2,0,0,True)

try: 
    asserter(3.1, [7,3], find_ten([7,3,9]), False)
    asserter(3.2, [5,5], find_ten([5,5]), False)
except:
    asserter(3, 0,0, True)

try:
    asserter(4.1, [1,2], less_than_five([1,6,7], [2,8,9]), False)
    asserter(4.2, [1], less_than_five([6,7,8], [1,5,6]), False)
except:
    asserter(4, 0,0, True)

try:
    asserter(5.1, True, letter_in_word('t', "python"), False)
    asserter(5.2, False, letter_in_word('q', "java"), False)
except:
    asserter(5,0,0,False)

    
