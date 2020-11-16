##SMALL problems

## 1.) Madlib function

# def madlib(name,subject):
#     return print(f'{name}\'s favorite subject is {subject}.')

# madlib('Adam', 'History')


## 2.) C to F conversion

# def C_to_F(temp):
#     print((temp * 9/5) + 32)

# C_to_F(0)


# # 3.) F to C conversion

# def F_to_C(temp):
#      print((temp - 32) * 5/9)


# F_to_C(0) 

## 4.) is_even function

def is_even(num):
    if (num % 2 == 0):
        print('True')
        return True
    else: 
        print('False')

is_even(3)

## 5.) is_odd function

def is_odd(num):
    if (is_even(num) is not True):
        print('True')
        return True    
    else:
        print('False')

is_odd(13)

## 6.) only_evens function

def only_evens(nums):
    evens = []
    for num in range(len(nums)):
        evens.append(num % 2 == 0)
    print(evens)

only_evens([11,20,42,97,10])

## 7.) only_odds function

def only_odds(nums):
    odds = []
    for num in range(len(nums)):
        odds.append(num % 2 != 0)
    print(odds)
    

only_odds([11,20,42,97,10])