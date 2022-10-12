#Напишите программу, удаляющую из текста все слова, содержащие ""ава"".
# a = "аватарка привет ава что делаешь какая погода лаваш авария мама папа кошка"
# a = (a.split(" "))
# print(a)
# convertList = "".join(map(str,a[0]))
# print(convertList)
# for i in a:
#     convertList = "".join(map(str, a[i]))
#     print(convertList)
#     if (a[i]+a[i+1]+a[i+2]) == 'абв':
#         a.pop(i)

#Напишите программу, которая будет выводить нечетные числа из списка и остановится, если встретит число 139

# list=[2, 1, 6, 8, 7, 5,10, 100, 67, 139, 140, 51]
# for i in range(len(list)):
#     if list[i]%2!=0:
#         if list[i]==139:
#             break
#         print(list[i])

list=[2, 1, 6, 8, 7, 5,10, 100, 67, 139, 140, 51]
for item in list:
    if item%2!=0:
        if item==139:
            break
        print(item)
