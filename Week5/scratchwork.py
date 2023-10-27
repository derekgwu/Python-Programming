#groceries = ["tomato", "potato","chicken"]
#1-d array
integer = [1,2,3,4,5]
booleans = [True, True, True, False, False]

#groceries.append("carrot")
#groceries.remove("potato")
#groceries.clear()

"""
"vegatables
carrots
lettuce
spinach"


"""

bread = ["english muffins", "bagels", "bread"]
fruit = ["mangos", "pears", "apples"]
dairy = ["milk", "cheese"]

groceries = [bread, fruit, dairy]
for sections in groceries:
    print(sections)

print(groceries[0])
print(groceries[0][1])

"""
english muffins
bagels
bread
mangos
pears
apples
milk
cheese
"""

for items in range(0,len(groceries),1):
    for food in groceries[items]:
        print(food)






