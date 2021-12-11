import random


class Student():

    def __init__(self, imie, nazwisko, numer_albumu,):

        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_albumu = numer_albumu
        self.kierunek = None
        self.srednia = None
        self.stypendium = bool

    def wybór_kierunku(self):

        while True:

            wybor = input("Hej studencie! Wybierz swój kierunkek spośród poniższych: \n Finanse i Rachunkowość \n Ekonomia \n Zarządzanie\n").capitalize()

            if wybor == "Finanse i Rachunkowość":
                print("Wybrałeś/aś kierunek: Finanse i Rachunkowość")
                break
            elif wybor == "Ekonomia":
                print("Wybrałeś/aś kierunek: Ekonomia")
                break
            elif wybor == "Zarządzanie":
                print("Wybrałeś/aś kierunek: Zarządzanie")
                break
            else:
                print("Żle wybrałeś kierunek, wybierz jescze raz")

    def sredniastudenta(self):
        self.srednia = random.uniform(2,5)

    def sprawdzeniesredniej(self):
        if self.srednia > 4.7:
            self.stypendium = True
        elif self.srednia > 3:
            self.stypendium = False
        else:
            print("zostałeś wyrzucony z uczelni")
            del(self)


student1 = Student("Marcin", "Kowalski",456789)
student1.wybór_kierunku()
student1.sredniastudenta()
print(student1.srednia)
student1.sprawdzeniesredniej()
print(student1.stypendium)

student2 = Student("Kacper", "Wojtczak",114529)
student2.wybór_kierunku()
student2.sredniastudenta()
print(student2.srednia)
student2.sprawdzeniesredniej()
print(student2.stypendium)


student3 = Student("Kacper", "Wojtczak",114529)
student3.wybór_kierunku()
student3.sredniastudenta()
print(student3.srednia)
student3.sprawdzeniesredniej()
print(student3.stypendium)