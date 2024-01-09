class Person():
   def __init__(self, name, age):
       self.name = name
       self.age = age
       #could have other things like birthday, hair color etc.

   #let's add a method to show inheritance of methods as well
   def get_name(this):
       return this.name

class Student(Person):
    def __init__(self, name, age, grade):
       super().__init__(name, age)
       #you can add on additional variables, but always call the parent constructor first if needed    
       self.grade = grade
    
    def get_grade(this):
       return this.grade
    
person_example = Person("Joe", 20)
student_example = Student("Billy", 18, "12th")
#this prints Joe
person_example.get_name()
#this prints Billy
student_example.get_name()

#this prints out 12th
student_example.get_grade()
                