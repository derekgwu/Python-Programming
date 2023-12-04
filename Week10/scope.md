# Scope

## Introduction
We have seen methods and classes and how they can have variables located within them. But consider this example

```python
def change_name(first, last):
    first_name = first
    last_name = last

first_name = "John"
last_name = "Smith"

change_name("Alex", "Jacobs")
print(first_name + " " + last_name)
```

The output of this program is:
```C
John Smith
```

But why? Our method call was suppose to change the name, so why did it not do it? This begins our lesson into scope.

## Scope
Scope is the term that explains variable availibilty. In other words, variables declared in methods and classes can only be accessed within the class or method itself. This is known as local scope. Let's look at local scope a little deeper.

### Local Scope
Consider this program

```python
def x1():
    x = "x1 got printed!"
    print_this_x(x)

def x2():
    x = "x2 got printed!"
    print_this_x(x)

def x3():
    print_this_x(x)

def print_this_x(x):
    print(x)

x = "x3 got printed!"
x1()
x2()
x3()
```
which has the output:
```Linux
x1 got printed!
x2 got printed!
```

You'll notice that to determine which x gets printed, your computer looks for a local x first. In `x1` and `x2`, there is a *local* x declared, so that x gets printed. However, if there is no x declared in the function, it will search for a `global` x in this case. 

In the case of `x3`, there is an `x` declared outside the function making it global. Thus that gets printed *because there is no local `x`*. Local variables get priority over global variables.

### Global Scope
But suppose by the off chance, we need to access a global variable in a local function. Let's go back to the change name example. Consider this revised code.

```python
def change_name(first, last):
    global first_name
    global last_name
    first_name = first
    last_name = last

first_name = "John"
last_name = "Smith"

change_name("Alex", "Jacobs")
print(first_name + " " + last_name)
```

Now the output is
```bash
Alex Jacobs
```

This is because the `global` keyword tells the computer to access the global variable instead of making a local variable.