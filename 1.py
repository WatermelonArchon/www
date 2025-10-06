a=input("Введите числа: ").split()
ch=int(input("Введите цифру: "))
for i in range(0, len(a)):
    a[i]=int(a[i])
print(a)
match ch:
    case 0:
        for i in range(0, len(a)):
            a[i]=0
    case 1:
        for i in range(0, len(a)):
            a[i]=a[i]*2
    case 2:
        for i in range(0, len(a), 2):
            a[i]+=10
    case 3:
        for i in range(0, len(a), 3):
            if a[i]<0:
                a[i]=0
            else:
                if (i+1)%3==0:   
                    a[i]**=0.5    
    case _:
        print("Сумма всех элементов: ",sum(a))
print(a)