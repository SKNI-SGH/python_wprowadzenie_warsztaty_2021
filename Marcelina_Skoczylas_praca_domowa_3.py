#zadanie 1

i=1
j=1
k=1
ciag=[1,1]

while len(ciag)<50:
    k=i+j
    j=i
    i=k
    ciag.append(k)

print(ciag)


#zadanie 2

wpisane=str(input("Proszę wpisać dowolne słowa po przecinku "))
zmienne=wpisane.split(",")

def funkcja(*args):
    '''Funkcja sprawdza długość słów i usuwa te, które są za krótkie'''

    lista=[]
    lista2=[]
    wartosc = int(input("Proszę wpisać jakąś wartość "))

    for arg in args:
        lista.append(arg)
        dlugosc=len(arg)
        if len(arg)>wartosc:
            lista2.append(arg)

    procenty=(len(lista2)/len(lista))*100
    return procenty,lista,lista2

print(funkcja(zmienne))


#zadanie 3

liczby=list(input("Proszę wpisać liczby po przecinku: "))
unikalna_lista=[]
n=1
a=liczby[n]
unikalna_lista.append(liczby[0])
while n<len(liczby):
    if liczby[n]!=unikalna_lista[n-1]:
        unikalna_lista.append(a)
    n+=1