import random

#in the arr, all elements appear twice except for 1, return the element that appears once
def appear_twice(arr):
    for i in range(0, len(arr), 2):
        if arr[i] != arr[i+1]:
            return arr[i]
    return -1

print(appear_twice([0,0,1,2,2]))

#adds the numeric value of two strings together
"123", "20" "143"

def adding_str(str1, str2):
    str1_as_int = int(str1)
    str2_as_int = int(str2)
    str3 = str1_as_int + str2_as_int
    result = str(str3)
    return result

#determines whether a string is a palindrome or not

#for i in range(0, len(str), 1)
def palindrome(str):
    var = str
    reverse_str = ""

    for i in range(len(str) - 1, -1, -1):
        reverse_str += str[i]

    if reverse_str == str:
        return True
    else:
        return False
    

#determine whether the sum of all the numbers in arr1 equal the product of all the numbers in arr2

def balanced(arr1, arr2):
    #add everything in arr1
    product1 = 1
    for num in arr1:
        product1 = num * product1


    #add everything in arr2
    product2 = 1
    for num in arr2:
        product2 = num * product2

    #compare the two
    if product1 == product2:
        return True
    else:
        return False
    
def anagram(str1, str2):
    for char in str1:
        #flag variable
        for char2 in str2:
            #if char == char2:
                #set flag variable to true
        #check flag variable
            #flag variable is true = go back to top of loop
            #flag is false = return false
    #return True
    return 0
 
def asserter(test_case, exp, func, *args):
    try:
        ret = func(*args)
        if ret == exp:
            print("Test Case " + str(test_case) + " SUCCESS!")
        else:
           print("Test Case " + str(test_case) + " FAILED. We expected: " + str(exp) + " but you returned " + str(ret))
    except Exception as e:
        print("Test Case " + str(test_case) + f" had an exception: {type(e).__name__}: {e}")


def run_tests():
    asserter(1.1, "222", adding_str, "111", "111")
    asserter(1.2, "1345", adding_str, "1000", "345")
    asserter(1.3, "123", adding_str, "0", "123")
    asserter(2.1, True, palindrome, "racecar")
    asserter(2.2, True, palindrome, "i did did i")
    asserter(2.3, False, palindrome, "notpalindrome")
    asserter(2.4, False, palindrome, "rotatior")
    asserter(3.1, True, balanced, [1,2,3], [2,3])
    asserter(3.2, False, balanced, [1,2,4], [2,2])
    asserter(3.3, True, balanced, [1,2,3,4], [1,2,3,4])
    asserter(4.1, True, anagram, "angel", "glean")
    asserter(4.2, True, anagram, "cool", "loco")
    asserter(4.3, False, anagram, "anagram", "just no")

run_tests()