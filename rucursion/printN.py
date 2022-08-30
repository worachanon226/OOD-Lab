def print1ToN(n):
    if n <= 0:
        print("1 ",end="")
        return 
    else:
        if n-1>0:
            print1ToN(n-1)
        print(f'{n} ',end="")

def printNto1(n):
    if n <= 0:
        print("1 ",end=" ")
        return 
    else:
        print(f'{n} ',end="")
        if n-1>0:
            printNto1(n-1)

n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)