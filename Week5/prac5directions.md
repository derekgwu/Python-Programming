# Week 5 Project: Trick-or-Treat Simulator

## Introduction
With the halloween season coming up, I figured I would make this week's project halloween related. In this project, you will simulate three kids going trick or treating, and you will keep track the types of candy each child has and how much candy each person has. This will be represented by a 2-D array.

To help you visualize, the 2-D array will have three elements, each one being an array. In each element, the array will contain the child's name in the first element, how much candy the child has in the second element, and any element after that will be the name of the candy the child has.

For example:
```
children = [
    ["Jacob", 2, "Milky Way", "Snickers]
    ["Ian", 1, "Hersheys"]
    ["Charlie", 2, "Skittles"]
]
```
Note that the names of the candy should be unique. THat is if a child gets 2 Skittles, do NOT add Skittles twice. 

## What You'll Be Doing
Trick-Or-Treating in most neighborhoods last from 3:00PM to 8:00PM (usually). Following the directions given here, each hour something will happen, whether the child gets candy or something else. It is your job to transform the trick-or-treating adventure into code. This mini-project has two goals:
1. Practice using multi-dimensional arrays
2. Practice understanding requirements when you code

## Instructions

### 3:00 PM
This is the start of trick-or-treating for the children. For this assignment, you'll keep track of three children. You may name these children whatever you want, however they must have a name. 

At 3:00 PM the children are only meeting together. All children will start with empty bags. To pass the 1st hour test cases, you must:
- Add 3 new children with unique names to `children`
- Ensure that each child has no candy

### 4:00PM
At 4:00 PM, each child has successfully trick-or-treated through a couple streets by now. To pass the 2nd hour test cases, you must:
- Ensure one child has 6 candy
- Ensure two children have 8 candy
- Ensure that each child has received both Jolly Ranchers and Snickers

### 5:00PM
At 5:00 PM, another child who is a friend of the children you created joins the group. He has already been trick-or-treating since 3:00PM, so he already has candy. Additionally, the current group of three children have also been trick-or-treating for another hour, so they will also have more candy

To pass the 3rd hour test cases, you must:
- Create a 4th child with a unique name and add him/her to `children`
- Set the 4th child's candy count to 8
- Give the 4th child two unique kinds of candy
- Increase 1st-3rd child's candy count by 2

### 6:00 PM
At 6:00PM, the 3rd child's bag rips, spilling his candy everywhere. The 1st child offers to some of the 3rd child's candy for the remainder of Halloween. To pass the 4th hour test cases, you must
- Set the 3rd's child to half of its original value (if he had 6 pieces of candy, he should have 3)
- Remove 1 type of candy from the 3rd child
- Add the 3rd child's lost half to the 1st child

### 7:00 PM
At this hour, the group of children enter the rich neighborhood to get alot of candy. To pass the 5th hour test cases, you must:

- Double each child's candy amount *EXCEPT* the 3rd child
- Add 1 new type of candy to each child *EXCEPT* the 3rd child

### 8:00 PM
At this hour, all four children have gone home and they are sharing their share of candy. They are throwing out candy they can't eat or trading their candy. To pass the final hour of test cases, you must
- Remove Snickers from the 2nd child's candy types as he is allergic to peanuts
- Remove Jolly Ranchers from the 1st child and give it to the 4th child

## Where to Write Your Code
Make sure you write your code in between the comment and test case call, otherwise the test cases will not work! 

```
#3:00 PM

#your code goes here!

hour_one()

#4:00 PM

#your code goes here!

hour_two()
```