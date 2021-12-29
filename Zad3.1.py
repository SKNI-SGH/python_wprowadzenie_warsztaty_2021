

def ciagfibo(x, y):
    y1 = 0
    y2 = 1
    print(y1)
    print(y2)
    while x<49:
        y = y1 + y2
        y1 = y2
        y2 = y
        print(y)
        x = x + 1


    return("50 wyrazów ciągu fibonaciego")


print(ciagfibo(0, 1))


