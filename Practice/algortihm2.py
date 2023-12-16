#THE SEARCH API
"""
You will implement 4 methods related to specific searches. All searches
will be performed on numerical arrays. If a search cannot find the neccesary element
(i.e the array is empty), return -1 to denote an error
"""

def get_by_target(arr, target):
    return 0

def get_by_index(arr, index):
    return 0

def get_last(arr):
    return 0

def get_largest(arr):
    return 0

"""UNIT TESTS"""
def asserter(test_case, exp, func, *args):
    try:
        ret = func(*args)
        if ret == exp:
            print("Test Case " + str(test_case) + " SUCCESS!")
        else:
            print("Test Case " + str(test_case) + " FAILED. We expected: " + str(exp) + " but you returned " + str(ret))
    except Exception as e:
        print("Test Case " + str(test_case) + f" had an exception: {type(e).__name__}: {e}")

asserter(1.1, 1, get_by_target,[0,1,2], 1)
asserter(1.2, 3, get_by_target, [0,4,6,7,8,9], 7)
asserter(1.3, -1, get_by_target, [0,5,7], 2)
asserter(1.4, -1, get_by_target, [], 3)
asserter(2.1, 7, get_by_index, [0,7,2], 1)
asserter(2.2, -1, get_by_index, [0,1], 2)
asserter(2.3, 1, get_by_index, [1], 1)
asserter(3.1, 9, get_last, [0,1,2,3,4,5,6,7,8,9])
asserter(3.2, -1, get_last, [])
asserter(3.3, 3, get_last, [3])
asserter(4.1, 9, get_largest, [0,9,2,1,4,5,6,3,8])
asserter(4.2, -1, get_largest, [])
asserter(4.3, 5, get_largest, [5])
