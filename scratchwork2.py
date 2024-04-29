#given an array, the arr represents a waiting room of patients with a number representing 
#how many minutes they have been waiting. Ideally, we want to help people who have been waiting the longest
#return a new array that contains all the patients in the order they should be helped in

#i.e given [7,5,2,1,6], ret. [7,6,5,2,1]

def longest_line(arr):
    0

#given a 3-digit lock that only takes the inputs of 1,2,3, return the correct password
def crack_the_code(arr, answer):
    0

#given two arrs, find the common element between both of them
def similar(arr1, arr2):
    0

#given an arr, find the element that is not continous with the others
#i.e given [1,2,3,4,7,8], return index 3 as arr[3] = 7, and 7 does not come immediately after 4
def one_aftr_one(arr):
    0

#return true if a letter appears twice in a word, and false other wise
def appears_twice(word):
    0




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
    asserter(1.1, [7,6,5,2,1], longest_line, [7,5,2,1,6])
    asserter(1.2, [4,3,3,2], longest_line, [2,4,3,3])
    asserter(2.1, [1,3,2], crack_the_code, [1,2,3], [1,3,2])
    asserter(2.2, [2,1,3], crack_the_code, [1,2,3], [2,1,3])
    asserter(3.1, 3, similar, [1,2,3], [3,4,5])
    asserter(3.2, 5, similar, [3,5,4,2,1,3,5], [1,3,46,3,4,63,1,5])
    asserter(4.1, 3, one_aftr_one, [1,2,3,4,7,8,9])
    asserter(4.2, 1, one_aftr_one, [0,1,3,4,5,6])
    asserter(5.1, True, appears_twice, "passed")
    asserter(5.2, False, appears_twice, "the quick brown")
run_tests()

    
