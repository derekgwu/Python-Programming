def median(arr):
    if len(arr) % 2 == 0:
        num1 = len(arr) // 2
        num2 = len(arr) // 2 - 1
        sum = arr[num1] + arr[num2]
        return sum//2
    return 0

def longest_word(str):
    words = str.split(" ")
    max = ""
    for word in words:
        if len(word) > len(max):
            max = word
    return max



def find_second(arr, num):
    numbers = []
    for i in range(0, len(arr)):
        if arr[i] in numbers and arr[i] == num:
            return i
        else:
            numbers.append(arr[i])
    return -1

def check_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i - 1]:
            return False
    return True

def unmerge_words(str):
    word1 = ""
    word2 = "" 
    for i in range(0, len(str)):
        if i % 2 == 0:
            word1 += str[i]
        if i % 2 == 1:
            word2 += str[i]
    return [word1, word2]

def reverse(list):
    left = 0
    right = len(list) - 1
    while(left < right):
        temp = list[left]
        list[left] = list[right]
        list[right] = temp
        left += 1
        right -= 1
    return list  



def sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return arr
        
    return arr





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
    asserter(1.1, 3, median, [1,2,3,4,5])
    asserter(1.2, 4, median, [1,3,5,7])
    asserter(1.3, 0, median, [0])
    asserter(2.1, "longest", longest_word, "this is the longest word")
    asserter(2.2, "greenhouse", longest_word, "longest word is at the end now greenhouse")
    asserter(2.3, "double", longest_word, "this has double space now ")
    asserter(3.3, 2, find_second, [1,2,1], 1)
    asserter(3.4, -1, find_second, [1,2,3], 2)
    asserter(3.5, 4, find_second, [3,1,1,5,3], 3)
    asserter(4.1, True, check_sorted, [1,2,3,4,5])
    asserter(4.2, False, check_sorted, [1,2,3,4,6,5])
    asserter(5.1, [1,2,3,4,5], sort, [5,3,4,2,1])
run_tests()

    
