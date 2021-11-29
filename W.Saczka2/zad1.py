text = input("Podaj dowolny tekst ")
length = len(text)
i = 0
letters=[]

while i<length:
    if i==0:
        letters.append(text[i])
        print(text[i])
        i+=1
    elif text[i] not in letters:
        letters.append(text[i])
        print(text[i])
        i+=1
    else:
        i+=1
