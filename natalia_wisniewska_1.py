#Zadanie 1
A=5
B=10
A,B=B,A
print("A")
print(A)
print("B")
print(B)

# Zadanie 2
name=input("Podaj swoje imię: ")
weight_lbs=float(input("Podaj swoją wagę w funtach (lbs): "))
height_ft=float(input("Podaj swój wzrost w stopach (ft): "))

weight_kg=weight_lbs*0.453
height_m=height_ft*0.3048
BMI=weight_kg/height_m

zdanie=f"Witaj {name}, twoja waga wynosi {weight_kg} kg, a wzrost {height_m} m. Twoje BMI wynosi {BMI}."
print(zdanie)

lista=['name',height_m,weight_kg,BMI]
print(lista)

#Zadanie3
name=input("Podaj swoje imię: ")
surname=input("Podaj swoje nazwisko: ")
age=int(input("Podaj swój wiek: "))

programming_languages=[]
programming_languages=[item for item in input("Podaj znane Ci języki programowania, oddzielone przecinkami: ").split(", ")]

foreign_languages=[]
foreign_languages=[item for item in input("Podaj języki obce, którymi posługujesz się w biegłym stopniu, oddzielone przecinkami: ").split(", ")]

zdanie=f"Nazywam się {name} {surname}, mam {age} lat. Znam następujące jezyki programowania:{programming_languages} i następujące języki obce:{foreign_languages}"
print(zdanie)

print("Ilość znanych języków programowania:")
print(len(programming_languages))
print("Ilość znanych języków obcych:")
print(len(foreign_languages))