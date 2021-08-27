# quickpython

quickpython is the projects with simple codes to share and learn the basic of python
[the codes in github] (https://github.com/trungnemo/quickpython)

## Installation

- How to install python on window
- How to install and basically use  the Visual Studio Code 
- How to create a github account and instal git at the local

## Bài 1: Variables and String
Lean to
- understand a python variable
- how to declare a variable/ string variable
```python
s = "Welcome to quichpython"
# s is the name of a varibale of string type
print(f'This is the print function to show : {s}')
```
## Bài 2: Numbers and Math
```python
#1 Declar a Integer var
x = 37
y = 3 
#2  Python Arithmetic Operators
# -----
# Add, substract, multiply, devide
print(x + y)
print(x - y)
print(x * y)
print(x / y)
#Exponentiation: 36 * 36 * 36
print(x ** y) 
#Floor division: 37/3 = 12 (= 12 * 3  + 1)
print(x // y)
#Modulus: get the remainder 1
print(x % y)
# 3 Python Assignment Operators
x += 1
```
## Bài 3: python list
Lean to
- what is a list variable and how to use it
```python
#1 declare list
menu= ["Pancake", "Ramen", "Pho"]
print(menu)
```
## Bài 4: python dictionary
Lean to
- what is a dict
```python
#1 declare a dictionary ('key': value) pair
#   key must be unique, key is a string
#   value can be any data type
emails = {
    'ben': 'tao.thanh@gmail.com',
    'trungvan' : 'trungnemo@gmail.com'
}
print(emails)
print(emails['ben'])
```
``
# Bài 5: Controll Flow
Learn to
- if elif else
- for
- while
```python
#1 using if else to check if the number is even of odd
i = 10
if i % 2 == 0:
    print('i is even')
else:
    print('i is odd')
```
# Bài 6: python function
Learn to work with python function

```python
def sum(n1, *numbers):
    for nx in numbers:
        n1 += nx
    return n1
sum(1, 2,4,6,7,8)
```
# Bài 8: python class
Learn to work with python class

```python
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
```

## Contributing
[TrungNEMO](https://www.facebook.com/TrungNEMO)


## License
[MIT](https://choosealicense.com/licenses/mit/)
