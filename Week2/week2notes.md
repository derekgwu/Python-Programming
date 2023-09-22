# Week 2 - Learn How To Be a Programmer

## Introduction
Everytime we interact with a computer, we are interacting with someone's code (usually). It might not seem like it, but we take many things for granted. From banking to YouTube, everything has been automated to be as efficient as possible. All of our everyday convenience in technology has likely been the result of countless software design today

- THINK: What's a piece of technology that you use everyday that likely has code in it?

## Design, Compile, Execute!
As a programmer, we are usually tasked with a problem and have to develop a solution to it. At a high-level, we can break down our problems in software development into three stages:

### Design Time
For example, let's say we work for NASA and we want to (hypothetically) travel to Mars. We've identify our problem, and the answer might seem obvious (rocket ship). But design time is not just coming up with a solution. It's coming up with implementations (aka HOW are we building the rocket ship). Design time is breaking down our big problem into smaller (and more manageable) problems. This could be answering the mini questions
- How big of a rocket do we need?
- How much oxygen do we need?
- How much food do we need?

When it comes to software development, you'll want to spend 70-90% of the time designing. While it might seem like overkill, the more time you spend planning, the less time you'll have to spend coding and fixing your code. Because everytime your code breaks, you'll be back at design time.

### Compile Time
This is basically the "coding time". But what does compiling mean? To understand compiling, let's pretend instead of talking to a computer, you are talking to the newest foreign exchange student. His English is not great, so it's difficult to get through to him. But your best friends speaks his language, so he's able to communicate with you and translate your English. That's what your programming language does. It's a way for the computer to understand our human ideas. When you compile your code, it's essentially translating it into binary, or a language your computer is fluent in.

Compile time should be easy, if you did a good job in design time. Otherwise you'll be doing design time and compile time at the same time, and you'll work extra slow. This should only be about 25% of the time spent in the development process.

### Execution Time
Finally, after you have design your implementations and code, you are ready to run your code. Now, two things can happen here:

1. Your code works perfectly as intended! You are done
2. Your code breaks. (More common occurance)

If your code breaks, there are two different type of errors you'll get:

1. Syntax and compilation errors

This usually means you misspelled a variable name or made a typo somewhere. These are usually easy to fix as Python IDEs will tell you where the error is.

2. Implementation errors

These are more common and harder to fix. This usually means your code does not do what its supposed to do (for example, returning "odd" when its an even number). 

## Testing and Debugging
While I did mention there were three steps to developing code, this is step 3 1/2. It's important that our code runs, but it's even more important to make sure our code does what it's supposed to do.

For example, let's take 