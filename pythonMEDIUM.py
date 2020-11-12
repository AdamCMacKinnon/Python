amount = float(input('Total Bill Amount? '))
level_of_service = input('Level of Service? ')
split = int(input('Split how many ways? '))

if (level_of_service == 'great'):
    level_of_service = level_of_service.lower()
    tip = (amount * .2)
elif (level_of_service == 'fine'):
    level_of_service == level_of_service.lower()
    tip = (amount * .15)
elif (level_of_service == 'bad'):
    level_of_service = level_of_service.lower()
    tip = (amount * .10)
else:
    tip = 0
print(f'Tip Amount: {tip:.2f}')
total_amount = (amount + tip)
print(f'Total Amount {total_amount:.2f}')
split_amount = (amount / split)
print(f'Total amount per person {split_amount:.2f}')

coins = 0
done = False

while not done:
    print(f'you have {coins} coins')
    answer = input('Do you want another?')
    if answer == 'yes':
        coins += 1
    else: 
        done = True
print('bye')

width = int(input('Width? '))
height = int(input('height? '))

box_top = ("*" * width)
print(box_top)

for star in range(height):
    print("*" + " " * (width -2) + "*")

box_top = ("*" * width)
print(box_top)



# pyramid problem, thanks to Layne

print(" " * 5 + "*" * 1 + "\n")
print(" " * 4 + "*" * 3 + "\n")
print(" " * 3 + "*" * 5 + "\n")
print(" " * 2 + "*" * 7 + "\n")
print(" " * 1 + "*" * 9 + "\n")
