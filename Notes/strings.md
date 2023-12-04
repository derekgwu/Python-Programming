# Week 6: Strings and its Properties

## Introduction
While numbers are extremely useful in computing and code, not all applications of code are analyzing numbers. Sometimes we need to computing or display words for our applications. I'm sure you could think of many examples why Strings are useful in code.

## Strings: The Basics
If you recall from week 1, we said Strings are a *non-primitive* type. Thus, Strings are composed of primitive types. In reality, Strings are essentially **arrays of characters**. Thus, many properties we use for arrays are also applicable for Strings. Remember, you 

### Accessing Specific Positions
Suppose we had a String:
```
String sample = "Hello World"
```

Like arrays, if we call `print(sample[0])`, we print the 1st position of the array, which is `H` in our case

### Looping Through Strings
If we want to print every element in an array individually, we would use a `for` loop. If we want to print every letter in a String individually, we can still use a `for` loop. Using the `sample` variable again, we can call
```
for character in sample:
    print(character)
```

and we would print out:
```
H
e
l
l
o

W
o
r
l
d
```

### Checking the Length of a String
Recall to check the length of an array we use `len()`. It is no different with Strings. Using `sample` again, calling `print(len(sample))` would print `11`.


### Other Function Calls
There are many other function calls unique to Strings in Python. You can check them out here:
- https://www.w3schools.com/python/python_strings.asp

## Cool Things You Can Do With Strings
There are other many unique things related to Strings that are worth noting. 

### Concantenating Strings
This is known as string addition. In short if we wanted to theoretically "add" strings together, we can!

Consider this code:
```
str1 = "Hello "
str2 = "World"
str3 = str1 + str2
print(str3)
```

If we ran this snippet of code, we would get:
```
Hello World
```

Note, concantenating strings does not have to be variables. You can also do it as:
```
str3 = str1 + "World"
```
### Comparing Strings
In most programming languages, because Strings are non-primitive, you usually cannot use the `==` to compare Strings.

Python is different and you are allowed to use the `==` to compare Strings. For example, this code is valid
```
str1 = "yes"
if str1 == "no":
    print("These Strings are the same")
else:
    print("These Strings are not the same")
```

## Characters Versus Strings
As mentioned earlier, Strings are arrays of characters. Thus, it is worth our time to dive back into characters and study the properties of characters. 

### Characters are Just Numbers....kinda of
Everything in computers is just a series of numbers. Thus a,b,c... does not really exist in a computer. In a computer's memory, it stores characters and Strings as numbers. So how does it remember what letters was stored?

Your computer use a character's **ASCII** values to "remember" which characters are stored in memory. In short, each character has its own ASCII value. Each characters corresponding ASCII value can be found here:

- https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html

Note, characters are not limited to "A-Z". Everything on your keyboard bascially has an ASCII value. 

If you want to access a character's ASCII value, you'll need to use the `ord()` function, which gives you a number based on whatever character is given in its argument. For example, consider this piece of code:

```
val_of_a = ord('a')
val_of_b = ord('b')
val_of_misc = ord('-')

print(val_of_a)
print(val_of_b)
print(val_of_misc)
```

And if we ran this program, our terminal would output
```
98
97
45
```

Additionally because these are numbers, we can perform math on them as well. For example:

```
val_of_c = ord('c')
val_of_c += 1
#convert it back to a character
print(chr(val_of_c))
```

If we ran this program, the terminal would output `d`. 