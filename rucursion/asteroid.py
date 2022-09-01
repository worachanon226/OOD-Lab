def asteroid_collision(asts):
    
    def recur(n,l):
        if n == len(asts):
            return 
        if len(l) == 0:
            l.append(asts[n])
        elif asts[n] < 0 and l[-1] > 0:
            if abs(asts[n]) == abs(l[-1]):
                l.pop()
            elif abs(asts[n]) > l[-1]:
                l.pop()
                recur(n, l)
                return 
        else:
            l.append(asts[n])
        recur(n+1,l)
    
    l = []
    recur(0,l)
    return l

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))