1. 
a = 5 
b = 10
a+=5
print(a)

2.
imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
wiek = int(input("Podaj swój wiek: "))
jezyki_programowania = input("Wymień języki programowania z jakimi się zetknąłeś (po przecinku): ").split(',')
jezyki_obce = input("Wymień języki obce, którymi posługujesz się w stopniu biegłym (po przecinku): ").split(',')
f"Nazywam się {imie} {nazwisko}, mam {wiek} lat/a, znam {len(jezyki_programowania)} język/i programowania i {len(jezyki_obce)} język/i obce"

3. 
lista= []
imie = input(("Podaj swoje imię: "))
lista.append(imie)
waga_lbs = float(input(("Podaj swoją wagę (w lbs): ")))
wzrost_ft = float(input("Podaj swój wzrost (w ft): "))
waga_kg = round(waga_lbs*0.453,2)
lista.append(waga_kg)
wzrost_m = round(wzrost_ft*0.3048,2)
lista.append(wzrost_m)
bmi = round(waga_kg/wzrost_m**2,2)
f"Witaj {imie}, twoja waga wynosi {waga_kg} kilogramów, wzrost {wzrost_m} metrów, a wskaźnik BMI {bmi}"