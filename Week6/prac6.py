def encrypt(message):
    first = message[0]
    message = message[1:len(message)] + first
    empty_str = ""
    for i in range(0, len(message), 1):
        #message[i]
        int = ord(message[i])
        int += 3
        empty_str += chr(int)
    return empty_str
    


def decrypt(message):
    0

"""UNIT TESTS"""

def print_utest(test_num, expected, ret):
    if(expected == "" or ret == ""):
        return
    
    feedback = "Expected: " + str(expected) + " but your answer was: " + str(ret)
    
    if expected != ret:
        msg = "FAILED"
        print("Test Case " + str(test_num) + ": " + msg + " " + feedback)
    else:
        msg = "SUCCESS" 
        print("Test Case " + str(test_num) + ": " + msg)


#Test 1 - simple encryption
def test1():
    msg = "Hello World"
    ret = encrypt(msg);
    exp = "hoor#ZruogK"
    print_utest(1, exp, ret)

#Test 2 - long encryption     
def test2(): 
    msg = "this is a long string, and it should be hard ... to ... encrypt but if you encrypt all of it...then you will pass"
    exp = """klv#lv#d#orqj#vwulqj/#dqg#lw#vkrxog#eh#kdug#111#wr#111#hqfu|sw#exw#li#|rx#hqfu|sw#doo#ri#lw111wkhq#|rx#zloo#sdvvw"""
    ret = encrypt(msg)
    print_utest(2, exp, ret)
    
#simple decryption
def test3():
    msg = "hoor#ZruogK"
    ret = decrypt(msg)
    exp = "Hello World"
    print_utest(3, exp, ret)

#long encryption
def test4():
    msg = "klv#lv#d#wrxjk#phvvdjh#wr#ghfu|sw#exw111li#|rx#jhw#lw111|rxu#ghfu|sw11vkrxog111pd|eh00zrunw"
    ret = decrypt(msg)
    exp = "this is a tough message to decrypt but...if you get it...your decrypt..should...maybe--work"
    print_utest(4, exp, ret)

#tests encryption to decryption back to encryption
def test5():
    msg = "to infinity and beyond..."
    ret = encrypt(msg)
    ret = decrypt(ret)
    print_utest(5, msg, ret)
    


test1()
test2()
test3()
test4()
test5()


