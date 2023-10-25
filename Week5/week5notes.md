# Week 5 - Introduction to Arrays

## Introduction
Briefly in last lessons, we discussed how for loops are mostly used in the case of arrays. This lesson will quickly recap the concept of arrays and expand our knowledge with 2-D arrays.

## Arrays: The Basics
Arrays are a useful way to group primitive and non-primitive types and variables. As in your last assignment, consider the case with groceries: 
```
groceries = ["Apples","Banana","Carrots"]
```

This is an array of Strings. This can be replicated with integers, doubles, boolean, or any type. It is important to note that accessing each individual object requires you to start at 0 and count upwards from there.

### Useful Function Calls With Arrays
Python is very generous with resizing arrays and adding to them. In most coding languages, when an array is declared and intialized, the size of the array is fixed. In other words, when you declare the groceries list, it can only hold a certain number of food items. If you wish to hold more items than you declared, you'll need to declare a new array with a new size (usually bigger than the original) and copy over the data from the old array.

Luckily, Python will do all of this for you. Here are a couple commands that make adjusting arrays easier.

- `append` - This adds an element to the end of your array
- `pop(index)` - This remove the element at whatever index you specify. For example `array.remove(0)` would remove the 1st element in the list
- `remove(element)` - This searches for an element and removes it. An error occurs if it does not find the element.
- `clear()` - This removes every element in the array

Of course there are a lot more than the ones I have listed. A better list can be found at: 
````
https://www.w3schools.com/python/python_arrays.asp
````

## Extension on Arrays
Making a grocery list, but sometimes the list itself gets complex. Suppose you were drafting your grocery list, and you want to organize it more by grouping foods by their grocery section. This is a very common practice because it prevents you from looping around the grocery store.

So let's say our grocery list gets more complex, and we are shopping for more foods. 
Suppose we need these items:

```
bread = ["whole wheat", "white", "muffins"]
fruit = ["apples", "banana", "mango"]
dairy = ["milk", "yogurt", "cheese"]
```
That's great we are able to make three separate grocery lists, but we obviously want to only bring one grocery list to the store. Thus, we can make a grocery list of our three lists like so,
```
bread = ["whole wheat", "white", "muffins"]
fruit = ["apples", "banana", "mango"]
dairy = ["milk", "yogurt", "cheese"]

groceries = [bread, fruit, dairy]
```

This is what we can an **array of arrays**. It is a mouthful to say. More specifically, this is known as a **2-D Array**, whereas we are more used to **1-D Arrays**. 

Traversing our 2-D array is no different than traversing our 1-D array. We can obviously just use a for loop:
```
bread = ["whole wheat", "white", "muffins"]
fruit = ["apples", "banana", "mango"]
dairy = ["milk", "yogurt", "cheese"]

groceries = [bread, fruit, dairy]

for sections in groceries:
    print(sections)
```

This will print:
```
['whole wheat', 'white', 'muffins']
['apples', 'banana', 'mango']
['milk', 'yogurt', 'cheese']
```

Additionally, we can also print individual elements in our grocery list using the indices.
```
print(groceries[0])
```

This will print:
```
['whole wheat', 'white', 'muffins']
```

This is great! We can now group arrays together, which allows us to bundle information together. Additionally, we can now make non-symmetrical arrays. Suppose we wanted to make a 2-D array that held a person's name and how many video games they had. Obviously, everyone owns a different amount of video games.

Our 2-D array would look like:
```
video_games = [
    ["Adam", "Super Mario Galaxy", "COD"],
    ["John", "Minecraft"],
    ["Billy"]]
```

But let's go back to our grocery list again. Suppose we are in the grocery store itself, and we already shopped and got everything in dairy section. When our software prints out the items we need, we do not want it to print out the items we already have. Additionally, instead of printing out the items like:
```
['whole wheat', 'white', 'muffins']
['apples', 'banana', 'mango']
```

Maybe we want to print out the items like:
```
whole wheat
white
muffins
apples
banana
mango
```

This is where we use **nested for-loops**. Nested for-loops usually look like
```
for sections in range(0,2,1):
    for food in groceries[sections]:
        print(food)
```

Let's dive into the syntax of the nested for-loop. The first for-loop `for x in range(0,2,1):` creates a variable called `sections` that starts from 0 and stops at 2 (non-inclusive), incrementing by 1. You can think of the outer loop iterating through `groceries`, where each element is `bread`, `fruit`, `dairy`.

The inner loop `for food in groceries[sections]:`iterates through each section of our grocery list. Because each element in the groceries is an array, this means each element can be traversed by a for-loop itself.

## Recap
This was a large module to go through. Let's highlight the big points.
- Arrays are useful ways to bundle information together.
- Arrays in Python have useful function calls to add and remove elements
- 2-D arrays are useful in grouping arrays together.
- We can use nested for-loops to traverse 2-D arrays.

