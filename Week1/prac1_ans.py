#Question 1: Given a number, write a function that will return true if the number is even, false if the number
#is odd
def odd_or_even(num):
    if(num % 2 == 1):
        return False
    else:
        return True
    
    return True

#Question 2: Write a function that will return the average/mean of an array of numbers
def find_average(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    
    mean = sum / len(arr)
    return mean

#Question 3: Write a function that will return the largest number in an array of numbers
def find_maximum(arr):
    biggest = 0
    for i in arr:
        if(i > biggest):
            biggest = i
    
    return biggest

#Question 4: Write a function that, given a number, will determine if an array contains that
#number. Return true if the array contains the number, return false elsewise
def contains(arr, num):
    for i in arr:
        if(i == num):
            return True
        
    return False

#Question 5: Write a function that will print a name backwards (i.e if given Derek, you would print kereD)
def reverse_name(name):
    reversed_name = ""
    for i in range(len(name) - 1, -1, -1):
        c = name[i]
        reversed_name = reversed_name + c
    return reversed_name

#Question 6: Given two numbers (a base and power), write a function that will return the 
#base raised to that power (i.e if given base = 4, power = 2, you would return 4^2 which is 16)

def power_of(power, base):
    for i in range(1, power, 1):
        base = base * base
    return base

#Question 7 (HARD): Given an integer, determine if the integer is a palindrome. That is, 
#if you reversed the number, it would be the same number.

#For example, the integer 121 would return true because forwards and backwards its 121
#However, 172 would return false, because 172 backwards is 271.

def palindrome_number(num):
    num_string = str(num)
    left = 0
    right = len(num_string) - 1

    while(left < right):
        if(num_string[left] != num_string[right]):
            return False
        left += 1
        right -= 1

    return True



#***MAIN CODE: DO NOT TYPE ANYTHING BELOW THIS LINE***
#***///////////////////////////////////////////////***

#Helper functions
def print_arr(arr):
    for x in range (len(arr)):
        print(arr[x])

#Test Case 1////////////////////////////////////////


ans1 = odd_or_even(1)
ans2 = odd_or_even(4)
ans3 = odd_or_even(107203)

#Test Case 1.1
if(ans1 == False):
    print("Test Case 1.1: Correct")
else:
    print("Test Case 1.1 is Incorrrect. We expected False")

#Test Case 1.2
if(ans2 == True):
    print("Test Case 1.2: Correct")
else:
    print("Test Case 1.2 is Incorrrect. We expected True")

#Test Case 1.3
if(ans3 == False):
    print("Test Case 1.3: Correct")
else:
    print("Test Case 1.3 is Incorrect. We expected False")

#Test Case 2 /////////////////////////////////////////////////


arr1 = [5, 2, 2]
arr2 = [8, 9, 4, 3]
arr3 = [5, 2, 30, -1]
ans1 = 3
ans2 = 6
ans3 = 9

#Test Case 2.1
if(find_average(arr1) == ans1):
    print("Test Case 2.1: Correct")
else:
    print("Test Case 2.1 is incorrect. We expected " + str(ans1) + " but you returned " + str(find_average(arr1)))

#Test Case 2.2
if(find_average(arr2) == 6):
    print("Test Case 2.2: Correct")
else:
    print("Test Case 2.2 is incorrect. We expected " + str(ans2) + " but you returned " + str(find_average(arr2)))

#Test Case 2.3
if(find_average(arr3) == 9):
    print("Test Case 2.3: Correct")
else:
    print("Test Case 2.3 is incorrect. We expected " + str(ans3) + " but you returned " + str(find_average(arr3)))

#Test Case 3 /////////////////////////////////



arr1 = [1, 2, 3, 4, 5]
arr2 = [-100, -250, 1, -1000]
arr3 = [7, 7, 7, 7]
ans1 = 5
ans2 = 1
ans3 = 7

#Test Case 3.1
if(find_maximum(arr1) == ans1):
    print("Test Case 3.1: Correct")
else:
    print("test Case 3.1 is Incorrect. We expected " + str(ans1) + " but you returned " + str(find_maximum(arr1)))

#Test Case 3.2
if(find_maximum(arr2) == ans2):
    print("Test Case 3.2: Correct")
else:
    print("test Case 3.2 is Incorrect. We expected " + str(ans2) + " but you returned " + str(find_maximum(arr2)))

#Test Case 3.3

if(find_maximum(arr3) == ans3):
    print("Test Case 3.3: Correct")
else:
    print("test Case 3.3 is Incorrect. We expected " + str(ans3) + " but you returned " + str(find_maximum(arr3)))


#Test Case 4 ////////////////////////////////

#Test Case 4 ////////////////////////////////
arr = [1, 2, 3, 4, 5]
arr2 = []

#Test Case 4.1
if(contains(arr, 1) == True):
    print("Test 4.1 is Correct")
else:
    print("Test Cased 4.2 is Incorrect. We expected True")

#Test Case 4.2
if(contains(arr, -1) == False):
    print("Test 4.2 is Correct")
else:
    print("Test Cased 4.2 is Incorrect. We expected False")

#Test Case 4.3
if(contains(arr2, 1) == False):
    print("Test 4.3 is Correct")
else:
    print("Test Cased 4.3 is Incorrect. We expected False")



#Test Case 5 ////////////////////////////////////


str1 = "Derek"
str2 = "Booker"
str3 = "George Washington"
ans1 = "kereD"
ans2 = "rekooB"
ans3 = "notgnihsaW egroeG"
ur_ans1 = reverse_name(str1)
ur_ans2 = reverse_name(str2)
ur_ans3 = reverse_name(str3)

#Test Case 5.1
if(ur_ans1 == ans1):
    print("Test Case 5.1: Correct")
else:
    print("Test Case 5.1 is Incorrect. We expected " + str(ans1) + " but you returned " + str(ur_ans1))

#Test Case 5.2 
if(ur_ans2 == ans2):
    print("Test Case 5.2: Correct")
else:
    print("Test Case 5.2 is Incorrect. We expected " + str(ans2) + " but you returned " + str(ur_ans2))

#Test Case 5.3
if(ur_ans3 == ans3):
    print("Test Case 5.3: Correct")
else:
    print("Test Case 5.3 is Incorrect. We expected " + str(ans3) + " but you returned " + str(ur_ans3))


#Test Case 6 ///////////////////////////////////
pow = 2
base = 4
ur_ans1 = power_of(pow, base)
ans1 = 16

#Test Case 6.1
if(ur_ans1 == ans1):
    print("Test Case 6.1: Correct")
else:
    print("Test Case 6.1 is Incorrect. We expected " + str(ans1) + " but you returned " + str(ur_ans1))


#Test Case 7 ///////////////////////////////////////

#Test Case 7.1
num = 1358531
if(palindrome_number(num) == True):
    print("Test Case 7.1: Correct")
else:
    print("Test Case 7.1 is Incorrect. We expected True")

#Test Case 7.2
num = 5665
if(palindrome_number(num) == True):
    print("Test Case 7.2: Correct")
else:
    print("Test Case 7.2 is Incorrect. We expected True")

#Test Case 7.3
num = 289
if(palindrome_number(num) == False):
    print("Test Case 7.3: Correct")
else:
    print("Test Case 7.3 is Incorrect. We expected False")







