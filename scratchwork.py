#student variable

#student properties
"""
name
present or not
allergies
age
birthday

"""


student1_name = "John"
student1_present = True
student1_allergies = ["Peanuts"]
student1_age = 10



class Student:
    def __init__(self, name, birthday, age):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.present = True
        self.allergies = []

    #getter
    def getStudentName(this):
        return this.name
    
    def getStudentAge(this):
        return this.age
    
    def getStudentPresent(this):
        return this.present

    #setter
    def isPresent(this, isHere):
        this.present = isHere
    
    def changeAge(this, new_age):
        this.age = new_age
    
    def isAllergicToPeanuts(this):
        for allergy in this.allergies:
            if allergy == "Peanuts":
                return True


student1 = Student("John", "08/02/2006", 18)
student2 = Student("Timothy", "09/04/2003", 17)

print(student1.getStudentName())
print(student1.getStudentAge())

student2.isPresent(False)
student2.changeAge(19)
print(student2.getStudentPresent())

