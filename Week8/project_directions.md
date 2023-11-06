# Project 1: Video Game Data Analysis

## Introduction
This week and the next couple of weeks, we will be starting our first major project. It will consist of numerous parts that we will split up through the next couple of weeks.

### What is Data Analysis?
Python is one of the best languages to process large datasets and draw conclusions from them. Python is popular with data analysis because:
- Supports many libraries that can graph and plot data
- Lots of work with arrays and string, and Python syntax makes it easy to handle (i.e `append()`, `remove()`)
- Easy syntax allows anyone to use Python
- Does not really matter how fast the program works (Python is incredibly slow compared to other languages)

### What will we be doing?
In `data.txt` I have gathered from Wikipedia the dataset of the most popular video games (by games sold). We will be extracting information from this dataset and creating information from it. 
- Source: [Most Popular Video Games](https://en.wikipedia.org/wiki/List_of_best-selling_video_games)



## Table of Contents
All the parts will be split into milestones. Each week we will try and complete a milestone. All the milestones will be written here, so you are more than welcome to complete other milestones earlier. However, each milestone usually builds off the previous milestones, so do not go out of order
- [Milestone 0: Data Cleaning](#milestone-0-cleaning-the-data)
- [Unit Tests](#unit-testing)

## Milestone 0: Cleaning the Data
When analyzing large datasets, a common problem is that the data is not always formatted the way we wanted. For example, look at the first couple lines in `data.txt`:
```txt
Minecraft 300,000,000 Minecraft	Multi-platform	November 18, 2011
Grand Theft Auto V	185,000,000	Grand Theft Auto Multi-platform	September 17, 2013
```
The formatting is not that bad, but it could be better. For example, there are a lot of unwanted tabs and extra spaces that we could get rid of. This milestone will focus on removing them, and organizing the `data.txt` into a proper array.

Given to you in `project.py` are three lines of code:
```python
file = open(r'\Users\dchen\Desktop\CompSci\tutoring-files\Week8\data.txt')
src = file.read()
data = []
```

The first two lines are opening the `data.txt` and converting it into a string. Note, we will need to fix the file path so it reads from wherever `data.txt` is stored on your computer. The third line gives you an empty array to store the cleaned data in. 

I strongly suggest storing each game and its associated data as one string, and let `data` be an array of strings. In this milestone you have two requirements:
1. Remove any tabs in `src` and replace them with spaces
2. Separate each game into its own string

### Tips for Removing Tabs
Python has a handy function called `string.replace(old, new)`, which goes through `string` and replaces every instance of `old` with `new`. It returns the new string. 

For example,
```python
str1 = "Today will be a good day"
new_str = str1.replace("good","great")
print(new_str)
```

Output:
```
Today will be a great day
```

Tabs are represented by the character `\t`. 

### Tips for Parsing Each String
In `data.txt`, each game is already kind of separate (strong kind of). You'll notice each game is on it's own line in `data.txt`. So it would be great if we separate by line.

In any programming language, line breaks have their own character, `\n`. So to a computer:
```
Hello
World

Hello\nWorld
```

These are the same. Here's the basic outline for separating the string by the `\n`.
1. Use a loop to go through each character in `src`
2. Have a blank string variable that you add letters onto. Every character that isn't the `\n` character, you add onto the blank string
3. If the character is the `\n` character, add the concentanated string into `data` and set string back to blank.

In short, this milestone does not have a lot of code. But it can be harder to conceptualize. 

## Unit Testing