import random

y = random.randint(1, 10)


x = 0
z = 1
while x != y:
        x = int(input("Zgadnij liczbe od 1 do 10: "))
        if x == y:
            print("zgadłeś")
            print(f"Zgadłeś za {z} razem")
        else:
            print("nie zgadłeś")
            z = z+1





