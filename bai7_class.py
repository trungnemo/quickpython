#-----------------------------------------------------------------
#By TrungVan, On 20210815
#ToDo   : how to use a class in python
#Reference links
#   https://www.w3schools.com/python/python_classes.asp
#-----------------------------------------------------------------   
# 1 declare a simple class
class Student:
    def __init__(self, clsroom, name, grade, height):
        # This is the initialize function, that instance the attribute values for each object based on the Student class
        self.clsroom = clsroom
        self.name = name
        self.grade = grade
        self.height = height
    def show_name(self):
        print(f'The student name is {self.name.upper()}')
    def show_classroom(self):
        print(f'The class rome is {self.clsroom.upper()}')
    def show_grade(self):
        print(f'Grade of the student {self.name.upper()} is {self.grade}')
    def show_height(self, newheight):
        print(f'The height of {self.name.upper()} is {self.height}')
    def set_height(self, newheight):
        self.height += newheight
#2 Instance and object of a class
student1 = Student("Duc Thanh", "9A1", "B", 1.7)
student2 = Student("Le Nguyen", "9A1", "A",1.56)
print(student1)
print(student1.name)
print(student2)
# use the property of a class: name
print(student2.name)
# call the method of Student class
student1.show_name()
student2.show_grade()
student2.set_height(1.6)
print(f'The height of {student2.name.upper()} is {student2.height}')
student1.show_height()



