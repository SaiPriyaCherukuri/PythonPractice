
msg = 'welcome to Python 101: Strings'
print(msg)     # welcome to Python 101: Strings
print(msg+msg) # welcome to Python 101: Stringswelcome to Python 101: Strings
print(msg*2)   # welcome to Python 101: Stringswelcome to Python 101: Strings
print(msg,msg) # welcome to Python 101: Strings welcome to Python 101: Strings

msg='welcome to it\'s Python 101: Strings'
print(msg.upper())      # WELCOME TO IT'S PYTHON 101: STRINGS
print(msg.lower())      # welcome to it's python 101: strings
print(msg.capitalize()) # Welcome to it's python 101: strings
print(msg.title())      # Welcome To It'S Python 101: Strings

msg = 'welcome to Python 101: Strings'
print(len(msg)) # 30
print(msg.count('o')) # 3
print(msg.count('python')) # 0 - because it is case sensitive

# slicing
msg = 'welcome to Python 101: Strings'
    #  0123456789
print(msg[5]) # m
print(msg[-3]) # n
print(msg[2:]) # lcome to Python 101: Strings
print(msg[2:15]) # lcome to Pyth
print(msg[:7]) # welcome


# Exercise: 1 Welcome Ring To Tyler - in title case
print(msg[18],msg[:7].capitalize(),msg[-5:-1].capitalize(),msg[8:10].capitalize(),msg[13].capitalize()+msg[12]+msg[2]+msg[1]+msg[-5])

msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title())

# Exercise: print the same string back words
print(msg1[::-1].title()) # Relyt Ot Gnir Emoclew 1


# Printing multilined string
msg="""Dear Terry,,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""
print(msg)


# find, replace
msg='Welcome to Python 101: Strings'
print(msg.find('h')) # 14
print(msg.find('Python')) # 11
print(msg.replace('Python','Java')) # Welcome to Java 101: Strings

msg1 = msg.replace('Python','JavaScript')
print(msg1) # Welcome to JavaScript 101: Strings

# menbership - if exists
print('Python' in msg) # True
print('Python' not in msg) # False

# srting formatting
name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color.lower() + '!' 
msg1 = f'[{name}] loves the color {color.lower()}!' # function in Python to format without +
print(msg) # [TERRY] loves the color red!
print(msg1) # [TERRY] loves the color red!

# Exercise - Print name terry in captalized
msg2 = f'[{name.capitalize()}] loves the color {color.lower()}!' 
print(msg2) # [Terry] loves the color red!