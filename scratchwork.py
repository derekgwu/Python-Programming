class Square():
   def num_sides(this):
       print("I have 4 sides")

class Triangle():
   def num_sides(this):
       print("I have 3 sides")

class Hexagon():
   def num_sides(this):
       print("I have 6 sides")

shapes = [Square(), Triangle(), Hexagon()]
for shape in shapes:
    shape.num_sides()