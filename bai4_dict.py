#-----------------------------------------------------------------
#By TrungVan, On 20210814
#ToDo   : working with dicitonary
#   reference links
#-----------------------------------------------------------------   
#1 declare a dictionary ('key': value) pair
#   key must be unique, key is a string
#   value can be any data type
emails = {
    'ben': 'tao.thanh@gmail.com',
    'trungvan' : 'trungnemo@gmail.com'
}
print(emails)
print(emails['ben'])
#2 Add, Delere a key,value pair in a dictionart
#add
emails['trang'] = 'trangmk2012@gmail.com'
emails['tmp'] = 'tmp@gmail.com'
print(emails)
#delete
del email['tmp']
#check if key in a dictionary
print('trungvan' in emails.keys())
print('ben' in emails.keys())
#3 Nesting dictionary
contacts = {
    'ben':
    {
        'email':'ben@gmail.com',
        'yborn': 2007,
        'name': 'Thanh Ben'
    },
    'trungvan':{
        'email':'trungnemo@gmail.com',
        'yborn': 1975,
        'name': 'Trung Van'

    }
}
print(contacts['ben']['email'])
print(contacts['ben']['yborn'])
print(contacts['ben']['name'])