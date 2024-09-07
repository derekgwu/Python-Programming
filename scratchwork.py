### Numbers and functions
def compare(x, y):
  '''
  Return whichever argument is larger using if statements.
  '''


### Strings
def combineOr(a, b):
  '''
  Return a string in the form "a or b" where a and b are the input arguments.

  combineAnd("abc", "xyz") = "abc or xyz"
  '''
  return


### Array operations
def returnNextToLast(a):
  '''
  Return the next to last element in an array.
  '''
  return


def addApple(a):
  '''
  Add the string "apple" to the end of the input array and return it.

  addApple(["cat", "carrot"]) = ["cat", "carrot", "apple"]
  '''

  return


def findMax(arr):
  "Find the largest number in the array"
  return

def findI(str):
  "Return the index where the letter 'I' appears"
  return





 #Unit Tests
 
def asserter(test_case, exp, func, *args):
    try:
        ret = func(*args)
        if ret == exp:
            print("Test Case " + str(test_case) + " SUCCESS!")
        else:
           print("Test Case " + str(test_case) + " FAILED. We expected: " + str(exp) + " but you returned " + str(ret))
    except Exception as e:
        print("Test Case " + str(test_case) + f" had an exception: {type(e).__name__}: {e}")


asserter(1.1, 7, compare, 7,6)
asserter(1.2, 9, compare, 6,9)
asserter(2.1, "abc or xyz", combineOr, "abc", "xyz")
asserter(3.1, 2, returnNextToLast, [4,3,2,1])
asserter(3.2, 7, returnNextToLast, [7,6])
asserter(4.1, ["banana", "orange", "yellow", "apple"], addApple, ["banana", "orange", "yellow"])
asserter(5.1, 5, findMax, [1,2,5,4,3])
asserter(5.2, 1, findMax, [0,-1,1])
asserter(6.1, 1, findI, "BILLY")

