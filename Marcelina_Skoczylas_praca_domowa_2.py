#zadanie 1
zdanie1=str(input("Proszę wpisać zdanie "))

i=0
while i<len(zdanie1):
    print(zdanie1[i])
    i=i+1


#zadanie 2
import random

losowa=random.randint(1,10)
wybrana=int(input("Proszę zgadnąć liczbę "))
liczbaprob=1
if wybrana!=losowa:
    while wybrana!=losowa:
        liczbaprob=liczbaprob+1
        wybrana=int(input("Niestety nie, spróbuj jeszcze raz "))
        print(f"Zgadłeś po {liczbaprob} próbach")

else:
    print("Zgadłeś po 1 próbie")



#zadanie 3

pary={
    "Afryka":59,
    "Ameryka Południowa":13,
    "Ameryka Północna":24,
    "Australia":14,
    "Azja":48,
    "Europa":46
}
kontynent=str(input("Proszę wpisać kontynent "))
kontynent2=pary[kontynent]
zdanie3=f"Kontynent ma {kontynent2} państw"
print(zdanie3)