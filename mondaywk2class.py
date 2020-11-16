## linking functions

# def funA():
#     return 0

# def funB():
#     result = funA() #0
#     print('')
#     return


# funBreturn = funB()

# def multiple(a, b, c):

#     return a * a, b * b, c * c

# var1, var2, var3 = multiple(c=2, a=5, b=8)

# print(var1, var2, var3)

#example of "early return"

# def square(side):
#     if side == 0:
#         return None
#         # dividing by 0 returns division error.  "if" statement calls early return and breaks code block.  
#         # allows to catch error rather than blowing up code.
#     return side / (2 * side)

# result = square(0)

# print(result)

# import random #called "modules"

# # random.randint(1,9) #generates random number between two listed numbers

# def getanswer(answerNumber):
#     if answerNumber == 1:
#         return 'it is certain'
#     elif answerNumber == 2:
#         return 'it is decidedly so'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'


# # r = random.randint(1, 9)

# # fortune = getanswer(r)

# # print(fortune)

# spam = 'global spam'

# globalA = 5 #outside the function.

# def someFunction():
#     localA = 5 #local scope (meaning it's in the function, not outside.  "in the black box")
#     global spam
#     spam = 'local spam'
#     print(spam)

# print(spam)

## all caps and snake case = signal to developers that these are constants.

# TAX_RATE = .09  # 9 percent tax
# COST_PER_SMALL_WIDGET = 5.00
# COST_PER_LARGE_WIDGET = 8.00
# def calculateCost(nSmallWidgets, nLargeWidgets):
#     subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGET) + (nLargeWidgets * COST_PER_LARGE_WIDGET)
#     taxAmount = subTotal * TAX_RATE
#     totalCost = subTotal + taxAmount
#     return totalCost
# total1 = calculateCost(4, 8)  #  4 small and 8 large widgets
# print('Total for first order is', total1)
# total2 = calculateCost(12, 15)

## -------------------------- MEDIUM PROBLEMS

# num_list = [3, 8, 10, 45, 2]
# def smallest(num_list):
#     return (min(num_list))

# print(smallest(num_list))

# def largest(num_list):
#     a = num_list[0]
#     for num in num_list:
#         if num > a:
#             a = num
#     return a

# print(largest(num_list))

string_list = ['Benjamin', 'Sarah', 'Clayton', 'Alexander', 'Adam']

# def shortest(string_list):
#     a = string_list[0]
#     b = []
#     for letters in string_list:
#         if len(letters) < len(a):
#             b.append(letters)
#     return b

def longest(string_list):
    longest = ''
    for name in string_list:
        if len(name) > len(longest):
            longest = name
    return longest

print(longest(string_list))
# print(shortest(string_list))




