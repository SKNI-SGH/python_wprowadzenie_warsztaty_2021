# zad1
a = 5
b = 10

c = a
a = b
b = c

# zad2
kg=0.453
m=0.3048
name=input("Podaj swoje imię ")
weight=float(input("Podaj wagę w funtach "))
height=float(input("Podaj wzrost w stopach "))

BMI=kg*weight/(m*height)**2
lista=[name, kg*weight, m*height, BMI]

print(f"Hej {lista[0]}!, Twoja waga w kilogramach to {lista[1]}, Twój wzrost w metrach to {lista[2]}, wskaźnik BMI to {lista[3]}")


# zad3
name=input("Podaj swoje imię ")
surname=input("Podaj swoje nazwisko ")
age=int(input("Podaj swój wiek "))
foreign=input("Proszę wymienić, po przecinku, znane Ci języki obce ")
list1=foreign.split(',')
programming=input("Proszę wymienić, po przecinku, znane Ci języki programowania ")
list2=programming.split(',')

print(f"Nazywam się {name} {surname} i znam "+str(len(list1))+" języków obcych oraz "+str(len(list2))+" języków programowania")