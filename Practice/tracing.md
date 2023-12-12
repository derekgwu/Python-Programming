```python
class Cat:
    def __init__(self, whiskers, fur_color, weight):
        this.whiskers = whiskers
        this.fur_color = fur_color
        this.weight = weight
    
    def get_whiskers(this):
        return this.whiskers

    def get_fur_color(this):
        return this.fur_color

    def get_weight(this):
        return this.weight
    
    def set_weight(this, weight):
        this.weight = weight

    def print_cat(this):
        print(str(whiskers) + " " + fur_color + " " + str(weight))

tiger = Cat(8, "orange", 200)
house_cat = Cat(4, "white", 30)

tiger.print_cat()
house_cat.print_cat()

tiger_weight = tiger.get_weight()
print(tiger_weight)

tiger.set_weight(300)
print(tiger_weight)

tiger_weight = tiger.get_weight()
print(tiger_weight)

print(house_cat.get_fur_color)
house_cat = Cat(4, "gray", 40)
print(house_cat.get_fur_color)
```

```python
def method1():
    num1 = 7
    num2 = num1 + num1
    print(num2)
    print(str1)
    str1 = "hello"
    print(str1)
    method2(num1)
    print(num1)
    return

def method2(num1):
    num2 = num1
    print(num2)
    print(str1)
    str2 = str1 + "world"
    print(str2)
    return

num1 = 5
num2 = 6
str1 = "here"
method1()
method2()
```


