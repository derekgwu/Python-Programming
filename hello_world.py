
# This code should sum all even numbers between 1 and i.
def odd_num(i):
    sum = 0
    for num in range(1, i):
        if num % 2 == 1:
            sum += num
    return sum


# This code is supposed to find the largest number in the list.
def largest(numbers):
    
    max_number = 0

    for num in numbers:
        if num > max_number:
            max_number = num

    return max_number

def finddup(numbers):
    first_duplicate = None
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                first_duplicate = numbers[i]
                return first_duplicate
            
    return -1

def sort(numbers):
 
    sorted_numbers = []

    while numbers:
        smallest = min(numbers)  
        sorted_numbers.append(smallest)
        numbers.remove(smallest)
        

    return sorted_numbers


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
    asserter(1, 6, odd_num, 5)
    asserter(2, -1, largest, [-1,-3,-4,-5,-1])
    asserter(3, 2, finddup, [1,2,4,3,2,3,4,5])
    asserter(4, [1,2,3,4,5], sort, [1,5,4,3,2])
run_tests()