#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
print(friends)         # ['John', 'Michael', 'Terry', 'Eric', 'Graham']
print(friends_tuple)   # ('John', 'Michael', 'Terry', 'Eric', 'Graham')

## sets are unordered and does not entertain duplication of elements
print(friends_set)     # {'John', 'Michael', 'Terry', 'Eric', 'Graham'}


friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends_set.intersection(my_friends_set))   ## {'Eric', 'Graham'}
print(friends_set.difference(my_friends_set))   ## {'John', 'Michael', 'Terry'}

print(friends_set.union(my_friends_set))        ## {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Reg', 'Loretta', 'Colin'}



#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()
