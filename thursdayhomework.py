##MEDIUM

# problem 1

a = [2,4,7,10]
b = [4,8,9,5]

# newList = [(a[0] * b[0]), (a[1] * b[1]), (a[2] * b[2])]
# index = 0
newList = []



# for items in a:
#     newList.append(items * b[index])
#     index += 1

# print(newList)

# newList = []

for index in range(len(a)):
    newList.append(a[index] * b[index])

print(newList)

## SOLUTION FORM MATTHEW R:

# listA = [2, 4 ,5 ]
# listB = [3 ,4 , 9]
# newList =[0,0,0]
# x = 0
# while(x < 3):
#     newList[x] = listA[x] * listB[x]
#     x += 1
# print(newList)



## problem 2 solution from LAYNE

# list1 = [[1,3,5,6], [2,4,4,3]]
# list2 = [[5,2,1,0], [1,0,3,5]]

# add_list = []
# for row in range(0, len(list1[0])):
#     temp = []
#     for column in range(0, len(list1[0])):
#         temp.append(list1[row][column] + list2[row][column])
#     add_list.append(temp)
# print(add_list)

# twoDimList1 = [ [1, 3], [2, 4] ]
# twoDimList2 = [ [5, 2], [1, 0] ]
# result = [ [0, 0], [0, 0] ]
# for outterIndex in range(len(twoDimList1)):
#     for innerIndex in range(len(twoDimList1[outterIndex])):
#         result[outterIndex][innerIndex] = twoDimList1[outterIndex][innerIndex] + twoDimList2[outterIndex][innerIndex]
# print(result)