#-----------------------------------------------------------------
#By TrungVan, On 20210812
#ToDo   : working with list
#   reference links
#-----------------------------------------------------------------   
#1 declare list
food = ["Pancake", "Ramen", "Pho"]
print(food)
#   another way to declare list
customers = list(["John", "Peter", "Elon"])
print(customers)
#   empty list
meals = list()
print(meals)
#2 List index start with 0
print(food[0])
print(food[1])
print(food[2])
#3 Update list
food[1] = "Noodle"
print(food)
#4 Check if a member is in the list
numbers = [3,4,2,8,9]
print(4 in numbers)
print(1 in numbers)
print(9 in numbers)
#use var to keep the check in
found = 4 in numbers
print(found)
#5 Basic function list of number
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
#6 Add one , many...
#  add one
numbers.add(11)
print(numbers)
#  add multiple numbers
n2 = [8,11,6]
numbers.extend(n2)
print(numbers)
#   remove a value
numbers.remove(6)
print(numbers)
# how about 