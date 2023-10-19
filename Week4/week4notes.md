# Week 4: An Introduction to Loops and Arrays

## Introduction
Loops are an essential aspect of coding. It allows us to repeat lines of code without writing the same code over and over again.

For example, imagine if I was building a New Year's Eve countdown timer. To count the final seconds before the New Year without a loop, it would look like this:

```
#NYE TIMER

seconds_left = 10
print(seconds_left)
seconds_left -= 1

print(seconds_left)
seconds_left -= 1

print(seconds_left)
seconds_left -= 1

print(seconds_left)
seconds_left -= 1

print(seconds_left)
seconds_left -= 1

print(seconds_left)
seconds_left -= 1

print(seconds_left)
seconds_left -= 1

print(seconds_left)
seconds_left -= 1

print(seconds_left)
seconds_left -= 1

print(seconds_left)
seconds_left -= 1

print("HAPPY NEW YEAR")
```

Seems like a pain to write. Loops allow us to repeat lines similar to `print(seconds_left)` and `seconds_left -= 1`. Using a for-loop, the same code can be rewritten as:

```
for x in range(10,0,-1):
    print(x)

print("HAPPY NEW YEAR")
```

That's a lot easier! This is why loops are so powerul. The same thing can be performed using a while loop. 

```
seconds_left = 10
while(seconds_left != 0):
    print(seconds_left)
    seconds_left -= 1

print("HAPPY NEW YEAR")
```

Remember, all for loops are while loops. Let's take a look at the different types of loops.

## Types of Loops

#### While Loop

This is the most standard kind of loop. All loops are essentially while loops in disguise. Let's observe a while loop in this example:
```
while(password != expected_password):
    password = input("Enter password: ")
    if(password == expected_password):
        break
    else:
        print("try again")
```
While loops are best when there's a conditional needed. In this example, the program takes in a user's password and compares it to the expected password. The loop allows for the user to keep re-entering their password until they get it correct.

If we know how many times we want to loop in advance, we can use a for-loop instead

#### For Loop for Arrays
The for loop is great when you are iterating in an array. Suppose you want to print out the items on your grocery list. You can perform this for-loop operation

```
grocery_list = ["apples", "banana", "carrots"]
for items in grocery_list:
    print(items)
```

Note the essential parts in the for-loop:
- `for` : The reserved word for that denotes that the following operation is a for-loop
- `items` : This is a variable name that is defined when the for loop is executed. Note `items` can be replaced with any valid variable name, such as `x`, `i`, etc. Each element in the array is denoted by `items`.
- `grocery_list`: This is the array you are iterating through. Note, that the array must be created before you loop through it.

But suppose you did not have an array, and you need to use a for-loop. Then what?

#### For Loop: In Range
This is a special for loop that offers customizable options for the developer. Let's recall the New Year's Timer in this example:

```
for x in range(10,0,-1):
    print(x)

print("HAPPY NEW YEAR")
```

The key words `for` and `x` serve the same purpose as in the first for loop example. However, what does the in range do?

The `in-range` takes three numbers in a specified order. The first number (`10`) is the starting number. The second number (`0`) is the number to stop at. The third number (`-1`) is the step length per loop. In this case, the loops subtracts 1 from the starting point each loop.

## Dangers of Looping
Loops are great, but they can come at a hefty price if used incorrectly. Take this code for example:
```
while x < 10:
    print("The program is still running")
```

Note, that the variable x is never decreasing in the loop. Thus `x` will never be less than 10, and we will stay in the while loop forever. This is known as an *infinite loop* and our program runs forever. This is extremely bad and usually requires the user or developer to manually kill the program or terminal.

