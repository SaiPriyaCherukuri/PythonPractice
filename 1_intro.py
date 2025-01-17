# Printing variables
failed_subjects ='2'
name = 'John'
print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
print(name + '  will need to redo ' + failed_subjects + '  courses.')
name = 'Eric'
print(name + '  is doing well in geography.')

# datatypes and typecasting
is_going_out = False # boolean
a = "it's"
b = 'it\'s' # example escape chars

print(type('hello')) # str
print(type(1))       # int
print(type(1.64))    # float
print(type(True))    # bool

a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
c1 = int(float("3.4"))  # c1 will be... 3 after float typecasting
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'

print([a,b,c,c1,d,e,f,g,h,i,j]) # [1, 2, 3, 3, 1.0, 2.5, 3.0, 4.23, '80s', '22', '3.01']

print('Variables & Datatypes - Exercise')
#Create appropriate Variables for Item name, the price 
#and how many you have in stock

item_name = 'widget'
price = 23.5
inventory = 100
is_in_inventory = True
print(item_name, price, inventory, is_in_inventory) # widget 23.5 100 True