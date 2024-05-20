#calculate the n-th number in the fibonacci sequence
def fibonacci(n):
    first_prev = 1
    second_prev = 0
    current =  0
    for i in range(2,n):
        current = first_prev  + second_prev
        second_prev = first_prev
        first_prev = current
    return current

#calculate the result of a base raised to some power
def power(base, power):
    ans = 1
    for i in range(0,power):
        ans = ans * base
    return ans


#let arr be an array of 0s and 1s symbolizing dominos. Let 0 symbolize no domino and 1 symbolize
# a domino. Calculate the start index where we can knock over the most number dominos in one go
def dominos(arr):
    0


#given an arr, reverse it and return the new array
def reverse(arr):
    
    left = 0
    right = len(arr) - 1

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    
    return arr

#given an arr, alter the values such that it is all values in odd indices followed by values in even indices
def odd_to_even_2(arr):
    0
    
def factorial(num):
    return 0

def div_and_less():
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
    asserter(1.1, 3, fibonacci, 5)
    asserter(1.2, 34, fibonacci, 34)
    asserter(1.3, 0, fibonacci, 1)
    asserter(2.1, 16, power, 2, 4)
    asserter(2.2, 27, power, 3,3)
    asserter(2.3, 1, power, 2, 0)
    asserter(3.1, 2, dominos, [0,0,1,1,1])
    asserter(3.2, 1, dominos, [0,1,0,0])
    asserter(3.3, 1, dominos, [0,1,1,1,0,0,1,1])
    asserter(4.1, [1,2,3,4,5], reverse, [5,4,3,2,1])
    asserter(5.1, [1,3,5,7,0,2,4,6], odd_to_even_2, [0,1,2,3,4,5,6,7])
    asserter(6.1, 120, factorial, 5)
    asserter(6.2, 6, factorial, 3)
    asserter(7.1, [7,14,21, 28], div_and_less)
run_tests()

    
""""
for i to len(arr):
    highest_idx = -1
    if arr[i] == 1:
        j = i
        while(arr[j] == 1):
            streak += 1
            j += 1
        if highest < streak:
            highest = streak
            highest_idx = i
"""