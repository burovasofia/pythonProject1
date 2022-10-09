# print('Результат', 7, 15, end="\n" ) #end="\n" -это переход на новую строку
# print('Результат', 7, 15)
# print('Результат', 7, 15, sep="")
# print('Р\nе\nз\nультат') #\n переход на новую строку
# print(5**2) #Возведение в степень
# print(5/3) #Деление
# print(5//3) #Выделение целой части
# print(min(1,4,5,9,-3,4,0)) #минимальное значение
# print(max(1,4,5,9,-3,4,0)) #максимальное значение
# print(abs(-55)) #выводит положительное число
# print(pow(5,2)) #возведение в степень
# print(round(5/3)) #округление до ближайшего числа

#УРОК4
# num = 5
# del num #удалили переменную
# a = 5 #int
# b = 4.5 #float
# c = "hello" #string
# d = True # bool
# m = '5' #string
#
# print(b + str(a)) # преобразуем число в строку
# print(a + int(m)) # преобразуем строку в число

# num1 = int(input('введите первое число '))
# num2 = int(input('введите второе число '))
# if num1==5 and num2==6: #end чтобы условие выполнялось для обоих
#     print('yes')

# a='35687'
# b=0
# for i in a:
#     print(i)
#     b=b+1
# print("колличество символов", b)

# numbers = [5,2,7] # список(массив)
# numbers.append(100) # .append добавляем элемент в список
# print(numbers)

# numbers = [5,2,7] # список(массив)
# numbers.insert(1,"yes") # .insert добавляем элемент в список по определенному индексу
# print(numbers)

# numbers = [5,2,7] # список(массив)
# numbers.extend([5,6,8]) # .extend добавляем сразу несколько элементов в конец списка
# print(numbers)

# n = int(input("длина списка "))
# user_list = []
# i = 0
# while i<n:
#     string = "введите элемент " + str(i+1) + ": "
#     user_list.append(input(string))
#     i = i+1
# print(user_list)

# word = 'Football, basketball, skate'
# hobby = word.split(', ')
# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()
# print(hobby)

# country = {4:3}
# print(country[4])

# data = input('Введите текст: ')
# file = open('data/text.txt', 'a')
#
# file.write(data + '\n')
#
# file.close()

# file = open('data/text.txt', 'r')
#
# print(file.read())
#
# file.close()

# try:
#     x = int(input('Введите число: '))
#     x +=5
#     print(x)
# except ValueError:
#     print('Введите число!')

# x = 0
# while x == 0:
#     try:
#         x = int(input('Введите число: '))
#         x += 5
#         print(x)
#     except ValueError:
#         print('Введите число!')

# try:
#     file = open('data/text.txt','r')
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print('файл не найден')

# try:
#     with open('data/text.txt', 'r', encoding='utf-8' ) as file:
#         print(file.read())
# except FileNotFoundError:
#     print('файл не найден')