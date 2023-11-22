# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)



#remove all tabs in the string
#.replace()

str = "Hello My name is World"
#Hello My name is Booker
str = str.replace("World", "Booker")

str2 = "today is wednesday"
str2 = str2.replace("wednesday", "thursday")

print(str)
print(str2)

str3 = "Terraria	|44,500,000|	None	Multi-platform	May 16, 2011"
#"\t"
str3 = str3.replace("\t", " ")

#
print(str3)


#if this word is in this word, return true

str = "I like potatoes"

substring = "carrots"
substring2 = "potatoes"

if substring2 in str:
    print("yes!")


   




