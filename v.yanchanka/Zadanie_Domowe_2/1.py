string = str(input('Proszę wpisać tekst:'))
len_str = len(string)
i = 0
while i < len_str:
    for i in range(0, len(string)):
        flag = 0
        for j in range(0, len(string)):
            # checking if two characters are equal
            if (string[i] == string[j] and i != j):
                flag = 1
                break
        if (flag == 0):
            print(string[i])

    i+=1

'''
string="GeeksforGeeks"
 
for i in range(0,len(string)):
    flag=0
    for j in range(0,len(string)):
        #checking if two characters are equal
        if(string[i]==string[j] and i!=j):
            flag=1
            break
    if(flag==0):
        print(string[i],end="")
'''
'''
#simple
for char in list_1:
    print(char)

#advanced
list_1 = [print(char) for char in string]
'''

