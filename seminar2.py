#Сформировать список из N членов последовательности. Для N= 5 1,-3,9,-27,81
#print("Введите число N ")
#N = int(input())
#start = 1
#for i in range(N):
#    print(start, end=' ')
#    start *= -3

#N = int(input('Введите число '))
#for i in range(N):
#    print((-3)**i, end=" ")

#Ввести время в секундах и вывести часы,минуты,секунды
#N = int(input('Введите время в секундах '))
#ch  = int(N/3600)
#m = int((N-ch*3600)/60)
#s = int((N-ch*3600)-m*60)
#print(ch, "чч", m, "мм", s, "сс", )

#Узнайте у пользователя число N+NN+NNN пример N=3 считает 3+33+333
#N = (input("Введите число "))
#n1=int(N)
#n2=int(N+N)
#n3=int(N+N+N)
#sum = (n1+n2+n3)
#print(sum)

#N = int(input('Введите число: '))
#max=0
#while N%10>0:
#   a=N%10
#   if max<a:
#      max=a
#   N=N//10
#print(max)

#5-6 задача про прибыль и убытки
#V = int(input('Выручка: '))
#I = int(input('Издержки : '))
#if V>I:
#    print('Выручка больше издержек')
#    p=V/I*100
#    print('рентабильность выручки', p)
#   S = int(input('Колличество сотрудников: '))
#    P1 = p / S
#    print("Прибыль в расчете на одного сотрудника ", P1)
#elif V==I:
#    print("Работа в 0")
#else:
#    print('Издержки больше выручки')

#ЗАДАЧА 7 ПРО СПОРТСМЕНА

a = float(input("Сколько км пробежал спортсмен в первый день "))
b = float(input("Сколько км в день спортсмен пробежит "))
n=1
while a<b:
    a=a+a*0.1
    print(a)
    n = n + 1
print("Спортсмен пробежит ", b, " км на ", n, "день")
















