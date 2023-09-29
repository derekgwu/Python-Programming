# Week 3 Assignment - Are You Smarter Than a 5th Grader?

## Introduction
If you know the website Buzzfeed, they offer quizzes that people can fill out and get "results" of differing kind. This week's assignment will designing something of similar sorts. 

If you have never taken a Buzzfeed quiz, here's the link to take one and get a general idea of what we are designing: 
- https://www.buzzfeed.com/hazelyxlee/international-foods-european-vacation-quiz

However, we will be designing a quiz that has more direct right and wrong answers. In other words, users will be getting direct feedback whether they got the question right or wrong.

Additionally, this quiz can be about anything you are knowledgable about. Just don't be giving incorrect answers in your quiz.

## Requirements
However, there are some must-dos for this assignment. Your quiz should have at least the following content-wise:

1. A multiple choice question that takes answer choices A,B,C,D

    - Example: Who was the first president of the United States?
    - A. George Washington
    - B. Joe Biden
    - C. Donald Trump
    - D. Ronald Reagan
    - User would input A

2. A true or false question
    - Example: True or False: My name is Derek
    - True
    - False

    - User would input True. (*Note you can have them input other things but be sure to specify them in your program)

3. A fill-in-the-blank question 
    - Example: 2 + 2 = ___
    - User would input 4

4. A question that has more than one correct answer
    - Example: What colors are in the rainbow?

   -  User could input any valid color in the rainbow

The challenging, but optional, question type is write a two-part question where the second question
depends on the answer to the first question. Note if the user gets the first answer wrong, they CANNOT
have an attempt to answer the second question

In total you should have at least 6 questions in your test. There are no test cases in this assignment. With that being said, your code should be able test your code frequently as you can take your own quiz. Your code should be able to compile and run as intended.

In addition to the content requirements, you should also follow these coding-requirements:

1. Your code should run properly, and it should be able to take in user inputs and display outputs.

2. Your code should have proper variable names like we discussed and it should contain proper comments.

## Helpful Information
To make this assignment simple, this quiz will work within your terminal. Here are some help commands that you can use in your design:

- *print(...)* - Given a string value, this print out the string your terminal. If you want to turn a variable value into a string, put a *str()* in front the variable name when printing.

- *input(...)* - This takes a users input and assigns it to a variable. For example:
```
answer = input("Enter answer: ")
```

This takes a users input and store it in the variable answer. You can also have a message displayed with the input. 

Additionally if-else statements are a great way to determine whether an answer is right or wrong.