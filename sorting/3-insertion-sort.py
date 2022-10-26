def insertion(l):
    for i in range(1, len(l)):
        ele_i = l[i]
        for j in range(i, -1, -1):
            if ele_i < l[j-1] and j>0:
                l[j] = l[j-1]
            else:
                l[j] = ele_i
                break
        print(l)

inp = [int(i) for i in input("Enter Input : ").split()]
insertion(inp)