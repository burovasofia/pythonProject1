# 27.	Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# str = '156947'
# a = []
# for i in str:
#     a.append(int(i))
# print(a)
# print('Максимальное значение: ', max(a))
# print('Минемальное значение: ', min(a))


# str = '1 5 6 94 7'
# str = (str.split(' '))
# print(str)
# a = []
# for i in str:
#     a.append(int(i))
# print(a)
# print('Максимальное значение: ', max(a))
# print('Минемальное значение: ', min(a))

# 28.	Найдите корни квадратного уравнения ax² + Bx + C = 0 двумя способами:
# 1.	с помощью математических формул нахождения корней квадратного уравнения
# 2.	с помощью дополнительных библиотек Python

# import math
# a = int(input('введите число а: '))
# b = int(input('введите число b: '))
# c = int(input('введите число c: '))
# D = b*b - 4*a*c
# print('Дискриминант равен:', D)
# if D>0:
#     print('Уравнение имеет два корня: ')
#     D = math.sqrt(D)
#     x1 = (-b+D)/(2*a)
#     x2 = (-b-D)/(2*a)
#     print('x1 =', x1)
#     print('x2 =', x2)
# elif D < 0:
#     print('Уравнение корней не имеет!')
# else:
#     print('Уравнение имеет один корень: ')
#     x = (-b)/(2*a)
#     print('x =', x)

# 29.	Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# a = int(input('введите число: '))
# b = int(input('введите число: '))
# a1=a
# b1=b
# while a1!=b1:
#     if a1>b1:
#         a1=a1-b1
#     elif b1>a1:
#         b1=b1-a1
# nod=a1
# nok=int((a*b)/nod)
# print("НОК =", nok)

# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n+1
# Для n=6 {1:4, 2:7, 3:10, 4:13, 5:16, 6:19}

# n = int(input('введите число '))
# slovar = {}
# for i in range(1, n+1):
#     slovar.update({i:3*i+1})
# print(slovar)


