# Small Problem 1 and 2 combined
name = input('what is your name? ')

print('What is your name? ' + name + ' Hello, ' + name + '!' + str.upper(' your name has ' + 
str(len(name)) + ' Letters in it! Awesome!'))


# # Small problem 3
print('Please fill in the blanks below: \n' + '___(name)___\'s favorite subject in school is ___(subject)___')
name = input('what is name? ')
subject = input('what is subject? ')
# print(name + '\'s' + ' favorite subject in school is ' + subject)

# # Small problem 4 and 5 combined
day = int(input('Day (0-6)? '))
if (day == 0): 
    print('Sunday')
if (day == 1):
    print('Monday')
if (day == 2):
    print('Tuesday')
if (day == 3):
    print('Wednesday')
if (day == 4):
    print('Thursday')
if (day == 5):
    print('Friday')
if (day == 6):
    print('Saturday')
if (day == 0, 6):
    print('sleep in!')
else: 
    print('go to work!')

#Small problem 6
temp = int(input('Temperature in C? '))

temp_in_F = ((temp * 9/5) + 32)

print(round(temp_in_F, 1))
