# Week 4 Project: Grocery List

## Introduction
A common feature in applications is the ability to create a list. For example, take Google Docs. Google docs has ability to create bullet point that allow users to neatly organize their items. 

This week, you will be tasked with making an interactive grocery list. This software should be able to create a grocery list, add to the grocery list, and remove items from the grocery list once they are found. More specfic details can be found below.

## Requirements

### 1. Creating a New List
At the beginning of the program, a new array of Strings should be created (Note: Python allows for dynamic re-allocation so you do not have to specfic the size intially). You should 

### 2. Add Items To The List
The user should be able to add as many items to the list as possible until the user specifies `STOP` as a command. Every new entry should be added to the list, and the list should print an update version of the list. 

For example a common list could look like:
```
Apples
Bananas
Yogurt
Chips
```

And if I wanted to add `Carrots` to the list, I could type in `Carrots` and the new updated list would print out:

```
Apples
Bananas
Yogurt
Chips
Carrots
```

If I type `STOP`, then no more items can be added to the list. The list is finalized and we can begin removing items from the list.

### 3. Removing Items From The List
After all the items have been added, the list become finalized. Now, the user can type in items that are on the list to remove them. For example,

```
Apples
Bananas
Yogurt
Chips
Carrots
```

If I type: `Apples`, the new list would print out

```
Bananas
Yogurt
Chips
Carrots
```

If I type in `Potato` or any other item not in the list, print out an error message in addition to the updated list. 

### Helpful Notes
There are several loops you will need to implement in this project. I would suggest using for loops for printing out the list and while loops for taking user inputs. Note that Python has two helpful tools for adding and remove arrays

`array.append(str)` : This adds a string to the list

`array.remove(str)` : This removes a string from the list. 

*Note*: If you try to use `remove()` on an item that does not exist in the list, the program will **crash**. You will have to create a way to ensure that the item trying to be remove, exists intially.