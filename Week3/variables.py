#Practice With Variables

#What will print out???

#Problem 1
def problem_1():
    x = 8
    y = 9
    y = x
    y = y + 1
    print(y)

def problem_2():
    a = 6
    b = 5
    if(a < b):
        print(b)
    else:
        print(a)

def problem_3():
    d = 5
    e = 9
    if(d < e):
        d = e
        if(d == e):
            print("d equals e")
    else:
        print("d does not equal e")
    


problem_1()
proceed_1 = input("type to proceed to problem 2")
problem_2()
proceed_2 = input("type to proceed to problem 3")
problem_3()
