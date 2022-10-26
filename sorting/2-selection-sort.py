def selection(l):
    for last in range(len(l)-1,0,-1):
        mx, mx_i = l[0], 0
        for i in range(1,last + 1):
            if l[i] > mx:
                mx, mx_i = l[i], i
        if l[last] != l[mx_i]:
            l[last], l[mx_i] = l[mx_i], l[last]   
            print(f'swap {l[mx_i]} <-> {l[last]} : {l}')

inp = [int(i) for i in input("Enter Input : ").split()]
selection(inp)
print(inp)