#-----------------------------------------------------------------
#By TrungVan, On 20210815
#ToDo   : how to use a function in python
#Reference links
#-----------------------------------------------------------------   
#1 A case to introduce 20 persons
print("Hello, My name is Trung Van")
print("I am 36 years old")

print("Hello, My name is Ben")
print("I am 13 years old")
# What if there 20 persons to introduce, 
# repeat the codes 20 times!? the better way is to use function
def introduce(name, age):
    print(f'Hello, my name is {name}')
    print(f'I am {age} years old')

introduce("Trung Van", 36)
introduce("Ben", 13)
#2 Keyword parameters
introduce(age = 6, name = "Em Ong")
#3 basic paramters and return value function
def sum(x,y = 2):
    return x + y
print('Sample sum ' + str(sum(1)))
print('Sample sum ' + str(sum(3,5)))
# 4 global and local variables
number = 16 
def sum():
    print(f'inside  is {number}')
sum()
print(f'outside functions the value number is {number}')
number = 16 #global var 
def sum1():
    number = 20 #local var of sum1
    print(f'Inside, value number is {number}')
sum1()
print(f'Outside, value number is {number}')

number = 16 #global var
def sum2()
    global number
    number = 20 
    print(f'Inside, value number is {number}')
print(f'Outside, value number is {number}')
# 5 Variant length parameter samples
print('Trung Van', 'Mai Trang', "To Nhu", 'Ben', 'Em Ong')
def sum3(n1, *numbers):
    for nx in numbers:
        n1 += nx
    return n1

sum3(1, 2,4,6,7,8)