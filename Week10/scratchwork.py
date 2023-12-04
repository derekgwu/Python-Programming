

first_name = "John"
last_name= "Smith"
def change_name(first, last):
    global last_name 
    global first_name 
    first_name = first
    last_name = last




change_name("Alex", "Jacobs")
print(first_name + " " + last_name)