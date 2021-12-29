#zadanie 1
a=5
b=10
a=b
b=a
print(a)
print(b)


#zadanie 2
imie2=str(input("Prosze wpisać swoje imię "))
wagalbs=float(input("Proszę podać swoją wagę w funtach "))
wzrostft=float(input("Proszę podać swój wzrost w stopach "))

wagakg=wagalbs*0.453
wzrostm=wzrostft*0.3048
bmi=wagakg/(wzrostm*wzrostm)

zdanie2=f"Witaj {imie2}, twoja waga w kilogramach to {wagakg}kg, twój wzrost w metrach to {wzrostm}m, a twój wskaźnik BMI to {bmi}"
print(zdanie2)

lista=[imie2,wzrostm,wagakg,bmi]
print(lista)


#zadanie 3
imie3=str(input("Proszę podać swoje imię "))
nazwisko3=str(input("Proszę podać swoje nazwisko "))
wiek3=int(input("Proszę podać swój wiek "))
jezykiprogramowania3=str(input("Proszę wypisać po przecinku języki programowania, z którymi miałeś/aś styczność "))
jezykiobce3=str(input("Proszę wypisać po przecinku jęzki obce, które znasz w stopniu biegłym "))

ilejezykowprog=(jezykiprogramowania3.count(","))+1
ilejezykowobcych=(jezykiobce3.count(","))+1

zdanie3=f"Nazywam się {imie3} {nazwisko3}, mam {wiek3} lat, znam języki programowania: {jezykiprogramowania3} i języki obce: {jezykiobce3}"
print(zdanie3)
zdanie4=f"Znam {ilejezykowprog} języki programowania i {ilejezykowobcych} języki obce"
print(zdanie4)
