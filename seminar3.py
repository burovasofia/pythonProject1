#  Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2

# N = int(input('Введите число N '))
# a = []
# for i in range(N*-1, N+1):
#     a.append(i)
# print(a)
# p = 1

# num = input('Введите число ')
# sum = 0
# for i in num:
#     if i != ".":
#         if i != "-":
#            sum = sum + int(i)
# print(sum)

# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

# n = int (input('Введите размер списка '))
# import random
# list = list([random.randint(1,10) for i in range(0, n)])
# print(list)
# a = 6
# if a in list:
#     list.remove(6)
#     print(list)
# else:
#     print('Значения 6 в списке нет')


# 21.	Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.


# list = ["qwe", "asd", "zxc", "ertqwe", "qwe"]
# find = "qwe"
# count = 0
# for i in list:
#     if list[i] == find:
#         count = count+1
#         print(i)



# list = ["qwe", "asd", "zxc", "ertqwe", "qwe"]
# find = "qwe"
# print(list)
# find = list[0]
# count = 0
# for i in range(len(list)):
#     if list[i] == find:
#         count+=1
#         if count == 2:
#             print("Второе вхождение числа", i)
# Найти индекс повторяющего элемента
# a = ['1', 'af', '6', 'a', '4', 'af', '3']
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if(a[i]==a[j]):
#             print(a[j])
#             print(j)


