import statistics
import math
a=input("Введите числа: ").split()
ch=int(input("Введите цифру: "))
for i in range(0, len(a)):
    a[i]=int(a[i])
print(a)
aa=1
b=min(a)
c=max(a)
d=statistics.median(a)
match ch:
    case 0:
        print('Минимальный элемент: ', b)
        if a.count(b)>=2:
            print ('Количество минимальных значений:', a.count(b))
    case 1:
        print('Максимальный элемент: ', c)
        if a.count(c)>=2:
            print ('Количество максимальных значений:', a.count(c))
    case 2:
        for i in range(0, c-b):
            print(aa)
            aa+=c
    case 3:
        print(b) 
        for i in range(b, c-b):
            print(aa*c) 
    case _:
        print('Медиана списка: ', d)
        if d<=0:
            print('Факториал: 0')
        else:
            print('Факториал: ', math.factorial(d))        