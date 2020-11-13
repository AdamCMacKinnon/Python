# ##concatenate lists

# # a = [1, 2, 3, 4, 5]
# # b = [6, 7, 8, 9]
# # c = a + b

# # print(c)

# ## prints [1, 2, 3, 4, 5, 6, 7, 8, 9]



# ## append/extend lists

# # todos = ["pet the cat", "go to work", "shop for groceries", 
# # "go home", "feed the cat"]

# # additionalTodos = ['binge watch a show', 'go to sleep']

# # todos.extend(additionalTodos)

# # print(todos)

# # nums = [10, 2, 5, 8, 14, 50, 37]

# # print(nums)
# # ## prints list as its shown

# # del nums [0: 2]

# # print(nums)
# ## prints list without first two values

# ## SLICING

# # nums = [10, 4, 6, 38, 8, 2, 0, 1]
# # subList = nums[1:]

# # print(subList)
# # # ignores index 0, prints to the end of the list

# # nums.insert(3, 45)

# # print(nums)
# # ## adds 45 to third index of list.  Can add any data type (ie string, float, int, etc..)

# # nums.pop()
# # poppedElement = nums.pop()

# # print(nums)
# # print(poppedElement)
# ## prints list without ending 1.  poppedElement returns the item that was popped outside of the list


# # nums1 = [4, 6, 7, 8, 'nine', 5]

# # result = nums1.index('nine')

# # print(result)
# # prints 4, which is the first occurance of the item listed in the index function
# a = 1
# b = a

# print(b)

# c = [1, 2, 3, 4]

# d = c
# print(d)
# c[0] = 'changed'
# print(c)
# print(d)
## PRINTS: 1
# [1, 2, 3, 4]
# ['changed', 2, 3, 4]
# ['changed', 2, 3, 4]
## PASSING BY REFERENCE

#multi-dimentional lists

# matrix =[[0,1], [2,3]]

# matrix[0][1] #first bracket indicates which index, second indicates which element within the index

# print(matrix [0] [1])


# a = [ [2, 4, 6, 8 ],  
#     [ 1, 3, 5, 7 ],  
#     [ 8, 6, 4, 2 ],  
#     [ 7, 5, 3, 1 ] ]  

# outerIndex = 0
# innerArrIndex = 0
# while outerIndex <len(a):
#     print(a[outerIndex])
#     while innerArrIndex < len(a[outerIndex]):
#         print(a[outerIndex][innerArrIndex])
#         innerArrIndex += 1
#     innerArrIndex = 0
#     outerIndex += 1

## think of OUTER LOOP as an at-bat, and the INNER LOOP as the pitches in the at bat.  The at Bat has to complete before the
## the batter can change.

# alphabet = "abcdefghijklmnopqrstuvwxyz" #string
# index = 0
# while index < len(alphabet):
#     print(alphabet[index])
#     index += 1

# alphList=list(alphabet)

# alphJoin = ' '.join(alphList)
# print(alphabet)
# print(alphList)
# print(alphJoin)

# alph = list(alphabet)
# alph.reverse()

# print(alph)

# join = ''.join(alph)
# print(join)

# result = list(range(10))
# print(result)

# range(5, 20, 3) ## first is the starting point, second is the ending point UP TO but not including that value, third is increment


#FOR LOOPS

# names = ['Claude', 'Ian', 'Zach', 'Matthew', 'Kim', 'Susan']

# for nameElement in names:
#     print(nameElement)

# STRINGS

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# for letter in alphabet:
#     print(letter)

#RANGE
# for num in range(0,6):
#     print(num)

#RANGE w/ STEPS

# for num in range(0,10,2):
#     print(num)

#MULTIPLICATION TABLE

# for outer in range(1,11):
#     for inner in range(1, 11):
#         print(f'{outer} X {inner} = {outer * inner}')

