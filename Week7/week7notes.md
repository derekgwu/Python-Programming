# Week 7: Methods

## Table of Contents
- [Introduction](#introduction)
- [Encapsulation](#encapsulation)
- [Methods](#methods)
- [Arguments](#arguments)
- [Returning](#returning)
- [Project](#project-directions-mini-calculator)


## Introduction
Sometimes when we write very long complex code, there is a large amount of lines in our code. If you ever write more than 100 lines of code, it can be difficult to debug when something goes wrong. 

For example, let's say you were designing your own iPhone. iPhones can do many things, and let's pretend you are developing everything an iPhone can do. An iPhone can:
- Take pictures
- Text people
- Call people
- Hold apps
- Much more

Let's say in the design process, there's an issue with way the phone texts people. It would not make sense to look at the code that focuses on taking pictures. Additionally, we don't want any changes to the texting functions to affect our picture taking functions (assuming our camera works).

This is where the concept of **encapsulation** comes into play.

## Encapsulation
Encapsulation is the idea of bundling variables and functions that work together. For example, let's go back to the phone example and you had these variables:
```python
photos = [an array of photos]
txt_msgs = [array of strings]
missed_calls = an integer
contacts = [an array of arrays]
```

It would make sense to group contacts and text messages together and keep them away from photos. That way any changes we make to the contacts won't affect the photos. But how do we actually separate them?

## Methods
Methods are use to group blocks of code together. It uses the keyword `def` to create a method. You may have seen me use them a lot with unit tests where I'll write:
```python 
def unit_test1():
    if passed :
        print(you passed)
    else:
        print(you failed)
```
Then I'll write later on in the code, 
```
unit_test1() #this runs the block of code
```

To study the syntax with methods, let's use a more simple example:
```python
def adder(num1, num2): #1
    sum = num1 + num2 #2
    return sum #3

x = 2 # 4
y = 3 #5
result = adder(x,y) #6
```

Let's study the keywords when creating a method:
- `def` - This is the keyword used to when creating a funtion
- `adder` - Like variables, we have to give our functions names. This gives us a way to call functions later one
- `(num1, num2)` - These variables are known as *arguments*. These are essentially a set of variables that a function gets when its called. (View [arguments](#arguments) for a better understanding how arguments work)
- `return` - When the return keyword is used to, it stops whatever method is being run, and brings the code back to wherever the function was called. (View [return](#returning) to view how the `return` keyword works)

## Arguments
Recall our adder example.

```python
def adder(num1, num2): #1
    sum = num1 + num2 #2
    return sum #3

x = 2 # 4
y = 3 #5
result = adder(x,y) #6
```

In the parenthesis at line `1`, you can see there are two variables: `num1` and `num2`. These are two variables your function gets when it is called. In this case, `num1` and `num2` are the two variables you want to add together. 

Now what values are `num1` and `num2`? That is for you decide when the function is called. Let's look at line `6` where the function is called. Note that when the function is called, there are also arguments. The arguments in this case are `x` and `y`, which hold the values `2` and `3` respectively. 

Thus, when `adder(x,y)` is called, the arguments given are passed on. That is,
- `num1` gets the value of `x` or 2
- `num2` gets the value of `y` or 3

Note that order matters! If we said `adder(y,x)` instead of `adder(x,y)`, we would get
- `num2` gets the value of `x` or 2
- `num1` gets the value of `y` or 3

But let's stick with `adder(x,y)`. Now when the function is called, it jumps to line 1 (where `adder` is) and the block of code is executed. In this case, it simply adds whatever `num1` and `num2` are and stores it in a variable.


## Returning
Now that we understand how our method works, it would great to keep the results our addition. However, we cannot simply just say

```python
#arguments do not have to be variables
adder(3,2) 

#in adder(), there's a variable called sum!
#let's just grab that variable
print(sum) 
```

This is because the variables inside a method are only *alive* inside the method. That is once we reach the end of `adder()`, we lose access to `num1`, `num2`, and `sum`. So how do we keep the sum from our adder?

We can use the keyword `return`, which has two properties
- `return` ends the method when it is called, that is anything typed after return will not run (and in fact give you an error)
- You can say `return sum` to pass a variable back when the method returns. 

But where does this returned variable go? Notice in the `adder` example on line `6` we said
```python
result = adder(x,y)
```

When we return, the returned value will be stored in result. 

# Project Directions: Mini-Calculator

## Introduction
This week project is a little different than most project. This week, I have written out code that simulates a mini-calculator. It can perform the simple operations, such as addition, subtraction, multiplication, division. It can also perform also do more advanced operations like modulo and exponents.

However, the issue with my code is that it runs ALL of the operations at once. That is, if we wanted to add two numbers, it would also multiply the two numbers. We also have to change the variables for each number, if we want to calculate other numbers. We want our mini-calculator to work for any numbers we input.

## Your Job
You will organize each operation into their own method. Each method should take two numbers as arguments. For the exponential operation, it will take a base and power as argument. 

You will also organize your own tests for this assignment. These tests do not have to be formal like mine usually are, but I would like to see that you know how to call methods and passing arguments. For example, a simple test like this will be okay. 
```python
ret = addition(1,2)
print("Expected: 3")
print("Answer: " + str(ret))
```

In short, this assignment can be divided into two parts
- Organizing each operation into its own method
- Calling each method and checking they work