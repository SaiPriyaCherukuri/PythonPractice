#Tuples - faster Lists you can't change - they are immutable
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
print(friends)            # ['John', 'Michael', 'Terry', 'Eric', 'Graham']
print(friends_tuple)      # ('John', 'Michael', 'Terry', 'Eric', 'Graham')

## handling of lists and tuples is almost the same

print(friends[2])           # Terry
print(friends_tuple[2])     # Terry


print(friends[2:4])           # ['Terry', 'Eric']
print(friends_tuple[2:4])     # ('Terry', 'Eric')

## iterations and searches are faster on tuples when compared to lists because of them being less complex
## all the functions used for lists can be used on tuples except for functions like append, remove, pop 

## if you have data that you dont want to change throughout your program then its best to use tuple than a list

## there are also some secret magic ways to make tuple behave more like lists -- advanced, needs to be self researched