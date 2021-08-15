#-----------------------------------------------------------------
#By TrungVan, On 20210815
#ToDo   : import a custom module to use
#Reference links
#   https://www.w3schools.com/python/python_modules.asp
#-----------------------------------------------------------------   
# import bai8_module

# print(bai8_module.num_of_functions)
# name = 'Trung Van'
# name = bai8_module.upper(name)
# print(name)
# name = bai8_module.lower(name) 
# print(name)


import bai8_module as t
import bai7_class as std

print(t.num_of_functions)
name = 'Trung Van'
name = t.upper(name)
print(name)
name = t.lower(name) 
print(name)


hs1 = std.Student('Van Trung', '9A1', 'A',1.73)
hs1.show_height()