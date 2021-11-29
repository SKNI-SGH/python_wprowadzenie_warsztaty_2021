from random import randint

x=randint(1,10)

a = int(input("podaj liczbę z zakresu 1-10 "))
i=1

while a!=x:
    i+=1
    if a>x:
        print("x jest mniejsze, spróbuj ponownie")
    elif a<x:
        print("x jest większe, spróbuj ponownie")
    a = int(input("kolejna próba"))

print("brawo, zgadłes za "+str(i)+" razem")