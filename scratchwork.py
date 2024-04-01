def median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        middle_right = n / 2
        middle_left = middle_right - 1
        return (sorted_arr[middle_left] + sorted_arr[middle_right]) / 2
    else:
        middle_index = n / 2
        return sorted_arr[middle_index]

def longest_word(str):
    max = 0
    current_max = 0
    for i in range(0, len(str) - 1, 1):
        if str[i] == " " and current_max > max:
            max = current_max
            current_max = 0
        elif str[i] == " ":
            current_max = 0
        else:
            current_max += 1
    return max


def find_second(arr, num):
    found_first = False
    for i in range(0, len(arr) - 1, 1):
        if arr[i]== num and found_first == True:
            return i
        elif arr[i] == num:
            found_first = True
    return -1

def check_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i - 1]:
            return False
    return True


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
    asserter(3.3, 2, find_second, [1,2,1])
    asserter(3.4, -1, find_second, [1,2,3])
    asserter(3.5, 4, find_second, [3,1,1,5,3])
    asserter(4.1, True, check_sorted, [1,2,3,4,5])
    asserter(4.2, False, check_sorted, [1,2,3,4,6,5])
    asserter(5.1, [1,2,3,4,5], sort, [5,3,4,2,1])
run_tests()

    
