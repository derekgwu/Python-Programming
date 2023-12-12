# Algorithms (the basics)

## Introduction to Algorithms
We always want to write the best code possible. That is, we want to write code that is fast, yet effective (meaning it still performs the action we need it to). Currently, we have only been focusing on syntax of code. We have only studied keywords and learning how those keywords work. But, we have not been learned how to apply topics together. These next weeks will focus on using all the topics we have learned and applying them to solve basic problems.

## What is an Algorithm?
An algorithm is set a way to do something, in simple terms. Consider this code:

```python
def add_two(num):
    return num + 2

print(add_two(6))
print(add_two(8))
```

In this case we have written an **algorithm** that adds two to any number. In computing, algorithms are processes that have set instructions and perform an action.

## Coming Up With An Algorithm
The `add_two()` function is relatively simple and it is easy to think about. But let's think of a more complex algorithm. Let's say we need to come up with an algorithm that can identify all the even numbers in an array.

That's a little more complex. So do we write code for it? 

### 1. Ignore the Computer
How would I solve it as a human? If another person gave me five numbered cards, how would I identify which cards are even-numbered and which are not? 

## 2. Bring Back The Computer
Now that we have a human understanding for solving the problem, think about the constraints of a computer. In other words, what shortcuts do we take as humans that we can't really take in code?

## 3. Roughly Draft it Out
This can be writing code or writing pseudo-code (high level code that does not really compile). For low complexity problems, it's ok to write code and fail. 

## 4. Refine 
Once you start passing a couple test cases, you can start refining for edge cases and bugs. 