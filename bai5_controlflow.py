#-----------------------------------------------------------------
#By TrungVan, On 20210814
#ToDo   : control follow such as
#           if then else
#           
#   reference links
#-----------------------------------------------------------------   
#1 using if else to check if the number is even of odd
i = 10
if i % 2 == 0:
    print('i is even')
else:
    print('i is odd')
#2 check if the numer is > 10 and even or odd
iseven = i % 10
# +------------------------------+---------------------+
# |  Operator (other languages)  |  Operator (Python)  |
# +==============================+=====================+
# |              &&              |         and         |
# +------------------------------+---------------------+
# |              ||              |         or          |
# +------------------------------+---------------------+
# |              !               |         not         |
# +------------------------------+---------------------+
i = int(input('input the number!'))
if iseven and i > 10:
    print('even and > 10')
elif iseven and i <= 10:
    print('even and <= 10')
elif not iseven and i > 10:
    print('odd and > 10')
else:
    print('odd and <=10')
# 3 For loop
names = ["Ba Noi", "Trung Van", "Mai Trang", "To Nhu", "Duc Thanh", "Ut"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
# imagin you have 100 name in names, you type 100 lines of print, so we have for
for name in names:
    print(name)
#or we can use while
idx = 0
while idx M len(names):
    print(name)