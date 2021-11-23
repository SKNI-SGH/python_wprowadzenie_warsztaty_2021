continents = [{"Nazwa":"Europa","Liczba-krajów":46},
    {"Nazwa":"Azja","Liczba-krajów":50},
    {"Nazwa":"Ameryka-Południowa","Liczba-krajów":13},
    {"Nazwa":"Ameryka-Północna","Liczba-krajów":22},
    {"Nazwa":"Afryka","Liczba-krajów":57},
    {"Nazwa":"Australia i Oceania","Liczba-krajów":14},
]

user_text = input("Proszę wpisać kontynent\n")
result = 0
for continent in continents:
    if user_text == continent["Nazwa"]:
        result = continent["Liczba-krajów"]
        print(f"{user_text} ma {result} krajów")
        break
else:
     print("Nie udało się znaleźć takiego kontynentu")