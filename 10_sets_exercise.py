#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

#1
print('Eric' in friends and 'John' in friends)   # True
#2
print(friends.union(my_friends)) # {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Reg', 'Loretta', 'Colin'}
print(friends | my_friends)      # {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Reg', 'Loretta', 'Colin'}

#3
print(friends.intersection(my_friends)) # {'John', 'Graham'}
print(friends & my_friends)             # {'John', 'Graham'}

#4
print(friends.difference(my_friends))    # {'Michael', 'Terry', 'Eric'}
print(friends - my_friends)              # {'Michael', 'Terry', 'Eric'}

print(my_friends.difference(friends))    # {'Reg', 'Loretta', 'Colin'}

#5
print(my_friends.symmetric_difference(friends))   # {'Reg', 'Loretta', 'Colin', 'Michael', 'Terry', 'Eric'}
print(my_friends ^ friends)                       # {'Reg', 'Loretta', 'Colin', 'Michael', 'Terry', 'Eric'}

#6
cars_no_dupl =list(set(cars))
print(cars_no_dupl)          # ['900', '420', 'V70', '911', '996', 'V90', 'S', '328']