

x = open("losowy tekst.txt", "w")

x.write("kawiarnia w warszawie \nrestauracja w krakowie \npub w gdańsku \nuniwersytet we wrocławiu \n")

x = open("losowy tekst.txt", "r")

y = x.read()
c = y.split()


print(len(c))














