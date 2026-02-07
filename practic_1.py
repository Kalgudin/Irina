'''a = int(input("введите число: "))
b = int(input("введите второе число: "))

if a > b:
    print('первое больше второго')
elif a < b:
    print("второе больше первого")
else:
    print('Числа равны')

#Второй вариант

if a >= b:
    if a == b:
        print("Числа равны")
    else:
        print('первое больше второго')
else:
    print("второе больше первого")'''
from numpy import square

#from itertools import repeat

"""
s = input("введите два числа: ")

ar = s.split(' ')
print(ar)
if int(ar[0]) > int(ar[1]):
    print('первое больше второго')
elif ar[0] < ar[1]:
    print("второе больше первого")
else:
    print('Числа равны')
    """

'''
s = input("введите два числа: ")

ar = s.split(' ')
print(ar)


a = int(input("введите число: "))
b = int(input("введите второе число: "))
c = int(input("введите третье число: "))

s = 0
m = [a, b, c]

for i in m:
    if i > 0:
        s += i

print(s)
'''
# def inp_int(mas):
#     try:
#         mas.append(int(input("введите число: ")))
#         return True
#     except ValueError:
#         print('ValueError')
#         return False
#
# a = int(input('сколько вам нужно чисел? '))
# m = []
#
# for i in range(a):
#     while not inp_int(m):
#         pass
#
# print(m)

# s = input("введите строку: ")
#
# try:
#     print(int(s) ** 2)
# except ValueError:
#     print(len(s))
'''
def str_to_int(arr):
    i_ar = []
    for el in arr:
        if el.isdigit():
            i_ar.append(int(el))

    return i_ar

s = input("введите два числа: ")

ar = s.split(' ')
new_ar = map(int, ar)
print(ar)
print(max(ar))
print(min(ar))
print(sum(new_ar))
'''

# a = int(input('input '))
# b = int(input('input '))
# c = int(input('input '))
#
# s = 0
#
# if a > 0:
#     s =+ a
# if b > 0:
#     s += b
# if c > 0:
#     s += c
#
# print(s)

# a = input('input ')
#
# if a.isdigit():
#     print(square(a))
# else:
#     print(len(a))


# a = input('input ')
#
# s = list(map(int, a.split()))
#
# print(max(s))
# print(min(s))
# print(sum(s))
#
# if sum(s) > 100:
#     print('more 100')
























