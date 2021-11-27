#Zadanie 1
def split(tekst):
    return [char for char in tekst]
tekst=input("Wpisz tekst: ")
symbole=list(split(tekst))
index=0
while True:
    print(symbole[index])
    index=index+1
#Zadanie 2
import random

liczba=random.randint(1,10)
print(liczba)

print("Zgadnij cyfrę od 1 do 10")
proba=0
while True:
    liczba_uzytkownika=int(input("Wpisz swoją liczbę:"))
    if liczba_uzytkownika==liczba:
        print(f"Gratulacje, udało Ci się odgadnąć za {proba+1} razem!")
        break
    elif liczba_uzytkownika!=liczba:
        print("Spóbuj ponownie")
    proba+=1

#Zadanie 3
kontynenty={
    'Europa':46,
    'Azja':50,
    'Ameryka Południowa':13,
    'Ameryka Północna':22,
    'Afryka':57,
    'Australia i Oceania':14
}
pary=list(kontynenty.items())
kontynent=input("Wpisz kontynent ")
if kontynent in kontynenty:
    print("Kontynent ma {} państw".format(kontynenty[kontynent]))