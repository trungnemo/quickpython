#By TrungVan, On 20210811
#ToDo   : introduce the var of string type with basic functions
#   reference links
#   https://www.journaldev.com/24588/python-string-functions
#1 Declar a String var
varstr = "Welcome to Python Programming in 1 hour"
print(varstr)
name = "TrungNEMO"
#2 Concatenation
print("Hello " + name)
print("Hello " + name)
#string and int for the concatenation
name = 1
print(name)
#error can not concat the string and int
#print("value of name is " + name) # correct it by ustring str funtion
#3 Basic fucntion of String type
#3.1 convert to string
print("value of name is " + str(name))
#3.2 check if string is numeric
name = "1"
if name.isnumeric():
    print("total value plus 2 is " + str(int(name) + 2))

#3.3 length of string: how many character in string
print("Length of this string is " + str(len(varstr)))
#3.4 find a string in string
name = "Tao Duc Thanh"
idx = name.find("Thanh")
print(idx)
idx = name.find("thanh")
print(idx)
#3.5 Upcase and lowercase
name = "TAO DUC THANH"
if name.islower():
    print("Ten khong viet hoa " + name)
else:
    print("Ten viet hoa " + name)
#3.6 Count words in string
s = 'I like Python programming. Python is Awesome!'
print(f'Number of occurrence of "Python" in String = {s.count("Python")}')
#3.7 Input 
s = input('Please enter a string:\n')
if s.isnumeric():
    print("Not a string")
else:
    print(s.upper())
    print(s.lower())
    print(s)