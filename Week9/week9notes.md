# Week 9: Classes

## Introduction
We learned in week 7 that methods are effective ways to group and reuse code effectively. Methods are great at executing actions repeatedly with simplicity (recall the `adder()`). Now what if we want to group variables together, or create our own unique variables?

Consider we were coding an attendance sheet for a classroom, and we want to create a `Student` variable. This obviously does not exist in Python, but let's think about the properties a student might have in an attendance sheet. A `Student` will have a name (`String`), birthday (`String`), age (`int`), present (`boolean`). And that's just for one student. We will likely need to create multiple `Student` variables. 

With the knowledge we have right now, if we want to make multiple students we need to do something like...
```python
student1_name = "John"
student1_age = "10"
student1_present = True
student_birthday = "08/02/2006

student2_name = ...
student2_age = ...
student2_present = ...
student2_birthday = ...

student3_name = ...
student3_age = ...
student3_present = ...
student3_birthday = ...
```
You can see how this would get annoying rather quickly. Firstly it would be lead many variable naming confusion. 

## Classes: An Introduction
Classes are also known as non-primitive types or objects. Essentially, they are built from the primitive types. Let's look at an example of a class in Python.

```python
class Student
    def __init__(self, name, birthday, age):
        self.name = name
        self.birthday = birthday
        self.age = age

student1 = Student("John", "08/02/2006", 18)
```

That's a lot to take in. Let's break it down.

- `class Student` represents the class itself as a whole. Anything indented within it is in the class
- `def __init__` is known as a *constructor*. When we want to make a new instance of the class, we essentially call the constructor method. It will always take the argument `self`, but you do not need to pass it in when calling it.