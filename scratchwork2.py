#return true if all the elements in arr1 are in arr2, and false otherwise
def subset(arr1, arr2):
    return 0

#given two arrays, return all elements that appear in either arr1 or arr2 with no duplicates
def union(arr1, arr2):
    return 0

#given two arrays, return all elements that appear both in arr1 and arr2
def intersect(arr1, arr2):
    return 0


#given two arrays, return all elements that appear in set1 but not in set2
def set_diff(arr1, arr2):
    return 0

#HARD given two arrays, determine if all the elements in arr1 cannot be found in set2 and vice versa
#example arr1 = [1,2,3] arr2 = [4,5,6] return true
#example arr2 = [1,2,3] arr2 = [4,2,3] return false
def exclusive(arr1, arr2):
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
    asserter(1.1, True, subset, [1,2,3], [1,2,3,4,5,6])
    asserter(1.2, True, subset, [3,5,4], [5,2,3,7,4])
    asserter(1.3, False, subset, [1,5,6], [2,3,1,5])
    asserter(2.1, [1,2,3,4,5,6], union, [1,2,3],[4,5,6])
    asserter(2.2, [1,3,5], union, [1,3], [3,5])
    asserter(2.3, [1,2,3], union, [], [1,2,3])
    asserter(3.1, [1,2,3], intersect, [1,2,3,4,5,6], [-1,-2,-3,0,1,2,3])
    asserter(3.2, [], intersect, [], [1,2,3])
    asserter(4.1, [1], set_diff, [1,2,3], [2,3])
    asserter(4.2, [], set_diff, [1,2,3], [1,2,3])
    asserter(5.1, True, exclusive, [1,2,3], [4,5,6])
    asserter(5.2, False, exclusive, [1,2,3], [4,2,3])

run_tests()

    
