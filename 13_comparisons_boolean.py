a = 7      # assignment operators
b = 3
print(a == b)      ## False
print(a != b)       # True
print(a < b)        # False
print(a > b)        # True
print(a <= b)       # False
print(a >= b)       # True
print('o' in 'John')         # True - #membership
print('o' not in 'John')     # False


a = [3,7,42]
b = a
print(a == b)      # True
print(a is b)      # True -- #identity --  denotes that they are occupying same memory space in the computer
print(id(a), id(b))  ## 2 2 

a = [3,7,42]
b = [3,7,42]
print(a == b)      # True
print(a is b)      # False
print(id(a), id(b))    # 2 3 



print(int(True))     # 1
print(int(False))     # 0
print(bool('parrot'))  # True
print(bool(' '))  # True
print(bool(''))  # False
print(bool(42))  # True
print(bool(1))  # True
print(bool(0))  # False
print(bool([1,2,3]))  # True
print(bool([]))  # False

print(42 + True)      # 43
print(42 + False)     # 42