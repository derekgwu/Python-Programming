def median(arr):
    return 0

def longest_word(str):
    return 0


def find_second(arr, num):
    return 0

def check_sorted(arr):
    return 0


def sort(arr):
    return 0

def unmerge_words(str):
    return 0

def reverse_list(list):
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
    asserter(6.1, ["hello", "world"], unmerge_words, "hweolrllod")
    asserter(7.1, [1,2,3,4,5], reverse_list, [5,4,3,2,1])
    
run_tests()

    
