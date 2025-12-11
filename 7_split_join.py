
msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']

print(list(msg))        # ['W', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', '1', '0', '1', ':', ' ', 'S', 'p', 'l', 'i', 't', ' ', 'a', 'n', 'd', ' ', 'J', 'o', 'i', 'n']
# a method on string object which splits String apart into a list with white spaces
print(msg.split())      # ['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']

print(msg.split(' '), type(msg.split(' '))) # ['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join'] <class 'list'>

print(csv.split(','))      # ['Eric', 'John', 'Michael', 'Terry', 'Graham']

print(str(friends_list))         # ['Eric', 'John', 'Michael', 'Terry', 'Graham'] -- it looks lika a list but is actually a string
print('-'.join(friends_list))   # Eric-John-Michael-Terry-Graham  -- with a joining char '-'

print('-'.join(friends_list+friends_list))   # Eric-John-Michael-Terry-Graham-Eric-John-Michael-Terry-Graham
print(''.join(friends_list))           # EricJohnMichaelTerryGraham


msg ='Welcome  to  Python  101: Split  and Join'
print(msg.split(' '))          # ['Welcome', '', 'to', '', 'Python', '', '101:', 'Split', '', 'and', 'Join']

print(''.join(msg.split()))    # WelcometoPython101:SplitandJoin
print(msg.replace(' ', ''))    # WelcometoPython101:SplitandJoin




### EXERISE ### 
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)


friends_list = csv.replace(';',',').replace(':',',').split(',')
print('using replace' , friends_list)