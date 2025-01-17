# print user input
name= input('What is your name?: ')
print(name)      # a pop-up box that lets the user to enter a name and prints it

name = input('What is your name?: ')
age = input('What is your age?: ')
print('Hello '+ name + '! You are '+ age + ' years old.') # Hello Eric! You are 37 years old.

# build a calculator
num1=input('Enter a digit: ')
num2=input('Enter a second number:')
answer=float(num1)+float(num2)    # converting to float because the input is a string
print(answer)

# Exercise
# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name


name = input('Enter your name: ')
distance_km = input('Enter distance in km: ')
distance_mi = float(distance_km)/1.609

print('Hello '+ name.title() + '! Your distance is '+ distance_km + 'km. Your distance in miles is ' + str(distance_mi) +'miles.')

print(f'Hi {name.title()}! {distance_km}km is equivalent to {distance_mi} miles.')

# round distance in miles to 1 decimal
print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')