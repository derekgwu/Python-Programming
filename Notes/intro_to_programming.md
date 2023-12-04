# Week 2 - Learn How To Be a Programmer

## Introduction
Every time we interact with a computer, we are interacting with someone's code (usually). It might not seem like it, but we take many things for granted. From banking to YouTube, everything has been automated to be as efficient as possible. All of our everyday convenience in technology has likely been the result of countless software designs today

- THINK: What's a piece of technology that you use every day that likely has code in it?

## Design, Compile, Execute!
As a programmer, we are usually tasked with a problem and have to develop a solution to it. At a high-level, we can break down our problems in software development into three stages:

### Design Time
For example, let's say we work for NASA and we want to (hypothetically) travel to Mars. We've identified our problem, and the answer might seem obvious (rocket ship). But design time is not just coming up with a solution. It's coming up with implementations (aka HOW are we building the rocket ship). Design time is breaking down our big problems into smaller (and more manageable) problems. This could be answering the mini-questions
- How big of a rocket do we need?
- How much oxygen do we need?
- How much food do we need?

When it comes to software development, you'll want to spend 70-90% of the time designing. While it might seem like overkill, the more time you spend planning, the less time you'll have to spend coding and fixing your code. Because every time your code breaks, you'll be back at design time.

### Compile Time
This is basically the "coding time". But what does compiling mean? To understand compiling, let's pretend instead of talking to a computer, you are talking to the newest foreign exchange student. His English is not great, so it's difficult to get through to him. But your best friend speaks his language, so he's able to communicate with you and translate your English. That's what your programming language does. It's a way for the computer to understand our human ideas. When you compile your code, it's essentially translating it into binary, or a language your computer is fluent in.

Compile time should be easy if you did a good job in design time. Otherwise, you'll be doing design time and compile time at the same time, and you'll work extra slowly. This should only be about 25% of the time spent in the development process.

### Execution Time
Finally, after you have designed your implementations and code, you are ready to run your code. Now, two things can happen here:

1. Your code works perfectly as intended! You are done
2. Your code breaks. (More common occurrence)

If your code breaks, there are two different types of errors you'll get:

1. Syntax and compilation errors

This usually means you misspelled a variable name or made a typo somewhere. These are usually easy to fix as Python IDEs will tell you where the error is. Syntax is a fancy word for how we spell things.

2. Implementation errors

These are more common and harder to fix. This usually means your code does not do what it's supposed to do (for example, returning "odd" when it's an even number). 

## Testing and Debugging
While I did mention there were three steps to developing code, this is step 3 1/2. It's important that our code runs, but it's even more important to make sure our code does what it's supposed to do. How do we know our code does what it's supposed to do? We put our code to the "test" using test cases. 

For example, if you scrolled around the **prac.py** file, you might have seen this:

```
#Test Case 1////////////////////////////////////////
ans1 = odd_or_even(1)
ans2 = odd_or_even(4)
ans3 = odd_or_even(107203)

#Test Case 1.1
if(ans1 == False):
    print("Test Case 1.1: Correct")
else:
    print("Test Case 1.1 is Incorrect. We expected False")

#Test Case 1.2
if(ans2 == True):
    print("Test Case 1.2: Correct")
else:
    print("Test Case 1.2 is Incorrect. We expected True")

#Test Case 1.3
if(ans3 == False):
    print("Test Case 1.3: Correct")
else:
    print("Test Case 1.3 is Incorrect. We expected False")
```

These are test cases. In short, we give our code sample inputs and compare the code's outputs to their expected value. Using **if-else** statements is not the only way to test your code, but it's a good way to do it. 

### A small detour: edge cases

It's important to know that we cannot make "perfect" code. But thorough testing of code strengthens it and prevents the chance of any user breaking it. For example, take this sample code:

```
def findMax(arr):
    max = -999
    for x in arr
        if(x > max):
            max = x
    
    return max
```

This code, given an array of numbers, will output the biggest value in the array. But take the example **[0, 0, 0, 0]**. What's the max value? How does your program handle these *weird* cases? It's up to you to handle these. 

### Back To Scheduled Programming
Luckily, I'll write your test cases so you should not have to worry about thinking about edge cases for problems. However, you should get used to handling them. 

You won't pass test cases every single time. In fact, if that was the case, there's likely a problem with the test cases. So what happens when we fail our test cases?

### Debugging - Revisiting Steps 1-3 again
When we fail our tests, we take a step back and analyze what failed. Did we output the right message? Did we output anything? If we fail something along these lines, our logic is off and we must return to design time. If we make a syntax error, we return to compile time. 

That's why it's so important to spend as much time as possible at design time so we never have to return to it. However, things happen (and they will!), so be prepared. 

### How to Read Test Cases
Fortunately for you, I will make all your test cases, so you know what I am looking for. However, the test cases will always be attached to your assignment, and you can view each input and its expected output. For future projects, I will use my own testing method that looks like this:
```
def test(assertion, expected, test_num):
    if(assertion == expected):
        print("Test " + str(test_num) + ": SUCCESS.")
    else:
        print("Test " + str(test_num) + ": FAILED. Expected " + str(expected) + " but got " + str(assertion))


test(odd_or_even(10), False, 1.1)
```

You only need to focus on **test(odd_or_even(10), False, 1.1)**. But how do you read this? 

This enters a brief realm of classes, methods, and the idea of object-oriented programming. This is not exactly important for you to know now, but we will define what you need to know to understand test cases:

- **test**(...) - This calls my testing method and tests your code by giving it a sample input. It essentially says: "Hey, test this function with these numbers"
- **odd_or_even(10)** - This is the function that the tester runs. It won't always say **odd_or_even** but it will be the function that you wrote as a programmer. The **10** is the sample input value I am giving your function. In this example, I am giving your odd_or_even function the number 10 and asking it to output whether 10 is odd or even. This input value will always be in the parentheses next to your operation.
- **False** - this is the EXPECTED output. For example, we expect your code to output false as we know 10 is even.
- **1.1** -This is the test case number.
