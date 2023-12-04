# Project 2: A Mini Nintendo Switch

## Focuses:
- Classes
- Arrays
- Methods

## Table of Contents
- [Introduction](#introduction)
- [Milestone 1](#milestone-1---creating-users)


## Introduction
In this project you will be making your own mini Nintendo Switch. While you shouldn't expect to play the latest Mario Game on your mini-switch, you will be able to create and login into the switch as users and play terminal games on your switch.

Like the other projects, this project is broken down into 3 milestones.

## Milestone 0 - Creating Users
In this first milestones, you'll use your knowledge of classes and create mini Nintendo Switch Users. These users must take on the name `User` for you to pass the test cases. Each user has the following properties:
- An email
- A password
- A username
- A preferred language
- A list of games

When a new `User` is created, they will pass on an email, password, and username. At the start, the preferred language will be set to English and the list of games will be empty. (Take this as a hint for making your constructor)

In order to change the preferred language, your class of `User`s will need a setter that takes a String and sets that string. You should also have getters for all the variables in the `User` class. 




## Milestone 1 - Creating Games and Creating the ESHOP
For this milestone, we will create the `QuizGame` class. Each instance of `QuizGame` will have two methods: `__init__` and `play`. 

In `__init__`, you should take a String `name` as an argument and construct it in the method. For the `play` method, you should use your quiz from week 2. Thus, when the `play` method is called, your quiz will play. (This is essential for making the mini-switch work).

In addition, you will also build an e-shop. For this milestone, after you create the QuizGame class, create an instance of it and add it to the e-shop

## Milestone 2 - Running the Switch
This milestone is the most complex. Using an infinite while-loop, we will precisely develop a series of user inputs and outputs to "run the switch". Most of the inputs and outputs have been completed for you, but you will be responsible for creating a methods the switch needs. 

This milestone has no unit tests, as the test is your ability to log into the switch and interacting with it. 
