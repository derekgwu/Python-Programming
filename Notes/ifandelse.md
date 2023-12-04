# Week 3: A New Look At Variables and Understanding If-Statements

## Introduction
This week, we are going to take a better look at variables and understand how they work. Additionally, we will look at if-else statements and conditionals.

## A Deep Look Into Variables

### What are variables?
Variables are an essential part of mathematics. If you have not figured it out, computer science came from mathematics. All the binary you see in computers is all mathematics. 

You'll first see variables in a high school algebra class. Variables are used to solve equations when values are not known. In sense, they are values given names like *x* and *y* because their values **vary**. 

For example
```
5 = x + 3
```
We know that *x* equals 2 here.

But what about this example?
```
7 = 8 - x
```

In this example, *x* equals 1 here. We can see how *x* is used to solve equations where the values are not really known.


Variables take on a similar idea in coding. In short, we create names like *x* and *y* but we get CHOOSE what values they have. Additionally, the "values" do not have to be numbers (though for the rest of the notes I will stick to using numbers). However, we know that
```
x = 6
x = 'c'
x = "Hello World"
x = True
x = 7.89
```
 are all valid forms of code in Python.

### Variables in Code
Now that you understand we can choose values to assign to our variables, what if we want to change our variable values? For example, if we have 
```
x = 6
```

What if we need *x* to become 5? Let's imagine we have a box to understand what is going on. 

The box has a label **x** and inside that box is the number 6. We want to open up that box, take out the 6, and replace it with the number 5 (while still keeping the label **x** on it).

To do this, we can just say:
```
x = 5
```

Now our box **x** has the value 5 in it. It is important to note that a variable cannot hold two values in it. Thus, the value 6 has "disappeared". 

Now suppose we have TWO variables
```
x = 5
y = 8
```

We have TWO boxes now. But what if we wanted to put the value in **y** into x? Essentially, we want to put 8 into x. Granted we could do the same way we did in the previous example, but what if we did not know y equals 8? What if y was also changing throughout the program?

To make x have the same value as y, we say
```
x = y
```

While this looks like "x equals y" we are doing more than that. We are saying "x is assigned the value in y". The best way to understand this is by reading the code from right to left (i.e. the value on the right is assigned to the left) This leads us into a slight detour of the topic.

### State. No not the state you live in

When we run a program, a computer only knows the values of variables at that current line. For example, take this line of code:
```
x = 5 \\line 1
x = 4 \\line 2
```

Python reads line-by-line, so at line 1, the computer stores in its memory x = 4. However, when it reaches line 2, x becomes 5 and the computer has no memory that x was 4. 

The values our variables have at a certain time of the programming runtime are called state. For example, the state of the program is different at the start than at the end. 

### Back to Variables

Now that we have learned that variables can change values, what if we want to change a variable with a number to a variable with a character?

In most programming languages like Java and C, you declare a variable beforehand, in other words, you specify whether your variable *x* will hold integers, characters, or strings. So if you declare a variable as an integer type, that variable cannot hold characters, strings, etc.

However, that does not hold for Python because we do not declare our variable type. So the following code is perfectly fine:
```
x = 9
x = "Hello World"
```

This change from integer to string, or a change from one type to another, is known as casting. We cast a variable into another type, as we say. However, it is important to know the state of your program when you cast variables, as you can run into issues when casting. To extend on the code above,
```
x = 9
x = "Hello World"
y = x + 1
```

This will cause issues, as Python does not really know what "Hello World" + 1 means. 

## If-Else Logic

### Introduction to Boolean Logic
In order for computers to compute decisions, it needs to have something we can boolean logic. In short, a boolean variable is a variable that eithers hold true or false. This compared with if-else-statements allows decision-making in our programs, and it is what separates calculators from computers.

### Symbols Used In Comparisons

- == Equals
- != Does Not Equals
- < Less Than
- <= Less Than or Equal To
- \> Greater Than
- \>= Greater Than or Equal To

### If-Statements in Action

Consider this code:
```
x = 5
y = 7
if(x > y):
    print("x is bigger than y")
elif(x < y):
    print("x is smaller than y)
else:
    print("x is equal to y")
```
Let's focus on the if statement. An if statement consists of three parts
- if(...) - The word to denote an if-statement
- if(**x > y**) - The conditional. If the conditional is true, then it will enter the block of code within the if-statement
- print("x is bigger than y) - This is the block of code that will run IF the conditional is true. If the conditional is not true, the block of code will NOT run

### When To Use If, Else If, or Else

Now what about else and elif statements?

- *elif(...)* - These are paired with if statements. It allows you to essentially check a second conditional after the first if-statement.
- *else:* Additionally paired with if-statements. However, you'll notice else-statement do not have a conditional added onto them. Code written in else-statements will only run if ALL of the previous if and elif statements were false

You should note that elif and else statements are optional. It all depends on the code you are writing whether you need them or not. 

### Nested Conditionals
We can put if-statements within each other if we really want to.

Consider this code: 
```
x = 1
y = 2
z = 3
if(z > x):
    if(z > y):
        print("z is greater than x and y")
    else:
        print("z is greater than x)
else:
    print("z is the smallest)
```

If the first if-statement is true, it will enter the first block of code. Then we see inside that block of code another if-statement. If the second if-statement is true, then the second block of code will run.

However, nested conditionals are extremely disliked in the coding industry. Because you'll need to indent a lot for nested conditionals, it'll make your code harder to read, for you and others.

### Combining Conditionals
It is entirely possible to combine two potential if statements into one. For example, let's redo the code in the nested conditionals example from
```
x = 1
y = 2
z = 3
if(z > x):
    if(z > y):
        print("z is greater than x and y")
    else:
        print("z is greater than x)
else:
    print("z is the smallest)
```

to 
```
x = 1
y = 2
z = 3
if(z > x & z > y):
    print("z is greater than x and y")
else:
    print("z is the smallest)
```

Much cleaner. That is the usage of the "and" operator (which can also be ``` and```). Alternatively, there is the "or" operator denoted by ``` or```

```
x = 1
y = 2
z = 3
if(z > x or z > y):
    print("z is not the smallest")
else:
    print("z is the smallest)
```

## Recap
We went over a lot this week, and the assignment this week is pretty long. Thus, it is a good idea to recap what we just discussed:

1. Variables are names that take on values
2. Variable values can change throughout the program
3. Variable values can also change types thanks to casting
4. The state of a program is what variables' values are at a certain time in the program
5. Boolean logic is useful for decision-making in programming.
6. If-statements have a conditional and a block of code attached to them
7. If-statements can be followed by elif and else statements, but it is not required
8. Although not advised, we can nest our conditionals and have conditionals within conditionals
9. We can combine conditionals together to write cleaner code
