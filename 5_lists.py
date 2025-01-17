# print lists

friends = ['John','Michael','Terry','Eric','Graham']
#           0      1         2       3       4
print(friends)                           # ['John', 'Michael', 'Terry', 'Eric', 'Graham']
print(friends[1],friends[4])             # Michael Graham
print(friends[-1])                       # Graham
print(friends[2:4])                      # ['Terry', 'Eric']
print(friends[:4])                       # ['John', 'Michael', 'Terry', 'Eric']
print(friends[:])                        # ['John', 'Michael', 'Terry', 'Eric', 'Graham']

print(len(friends))                      # 5
print(friends.index('Eric'))             # 3
print(friends.count('Eric'))             # 1

# lists can have a mix of datatypes - strings, ints, booleans etc.,

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)                # ['John', 'Michael', 'Terry', 'Eric', 'Graham']

friends.sort()                ## sorts in ascending order
print(friends)                 # ['Eric', 'Graham', 'John', 'Michael', 'Terry']

friends.sort(reverse=True)    ## sorts in descending order, 'reverse' takes a boolean value
print(friends)                 # ['Terry', 'Michael', 'John', 'Graham', 'Eric']

friends.reverse()             ## just reverses the order of the list but does not sort it
print(friends)                 # ['Eric', 'Graham', 'John', 'Michael', 'Terry']

cars.sort()
print(cars)                    # [130, 308, 328, 535, 740, 911]

# min, max, sum
print(min(cars))               # 130
print(max(cars))               # 911
print(sum(cars))               # 2952

print(min(friends))            # Eric
print(max(friends))            # Terry
print(sum(friends))            ## TypeError: unsupported operand type(s) for +: 'int' and 'str'


## add new element to the list - append, insert or add at specific index
friends.append('Chris')
print(friends)                 # ['John', 'Michael', 'Terry', 'Eric', 'Graham', 'Chris']

friends.insert(1,'Chris')
print(friends)                 # ['John', 'Chris', 'Michael', 'Terry', 'Eric', 'Graham']

friends[2]='TerryG'            ## replaces the exising element at the index with new element
print(friends)                 # ['John', 'Michael', 'TerryG', 'Eric', 'Graham']

friends.extend(cars)          ## join 2 lists together or put 2 lists together
print(friends)                 # ['John', 'Michael', 'Terry', 'Eric', 'Graham', 911, 130, 328, 535, 740, 308]

# another way of joing lists - in this way we can join nay number of lists
# sales = sales_w1 + sales_w2


friends = ['John','Michael','Terry','Eric','Graham']
## remove items from the list - remove, pop or delete functions
friends.remove('Terry')
print(friends)                 # ['John', 'Michael', 'Eric', 'Graham']

friends.pop()                  ## pop command removes the last element of the list and keeps in cache 
                               ## so that value can be used in the program
friends.pop(-1)        # line 63 and 65 are same                       
print(friends)                  # ['John', 'Michael', 'Terry', 'Eric']

friends.pop(2)
print(friends)                  # ['John', 'Michael', 'Eric', 'Graham']

element = friends.pop()
element1 = friends.pop(-1)
print(element,element1)                 # Graham Eric

friends.clear()
print(friends)                    # []

del friends[2]                    # removes second element from the list

del friends                       ## its a bit more powerful so it is better to avoid using it
print(friends)                    # NameError: name 'friends' is not defined

## copying lists - 
friends = ['John','Michael','Terry','Eric','Graham']
new_friends = friends[:]
print(new_friends)                   # ['John', 'Michael', 'Terry', 'Eric', 'Graham']

new_friends = friends.copy()
print(new_friends)                   # ['John', 'Michael', 'Terry', 'Eric', 'Graham']

new_friends = list(friends)
print(new_friends)                   # ['John', 'Michael', 'Terry', 'Eric', 'Graham']