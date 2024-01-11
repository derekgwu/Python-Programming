def swap(arr, num1, num2):
    index = -1
    for i in range(0, len(arr)):
        if (arr[i] == num1 or arr[i] == num2) and index != -1:
            temp = arr[index]
            arr[index] = arr[i]
            arr[i] = temp
        if (arr[i] == num1 or arr[i] == num2):
            index = i
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

asserter(1, [1,3,2], swap, [1,2,3], 2, 3)
asserter(2, [2,1], swap, [1,2], 1, 2)
asserter(3, [7,2,3,4,5,6,1], swap, [1,2,3,4,5,6,7], 1, 7)
asserter(4, [1,2,5,4,3], swap, [1,2,3,4,5], 3, 5)
asserter(5, [1,9,2,7], swap, [1,7,2,9], 7, 9)
