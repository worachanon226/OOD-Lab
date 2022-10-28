def insertion(l, i, j):
    n = len(l)
    if i < n and j >= 0:
        if l[j] > l[j + 1]:
            temp = l[j + 1]
            l[j + 1] = l[j]
            l[j] = temp
        insertion(l, i, j - 1)
    if j == 0:
        insertion(l, i + 1, i)
    return l

inp = [int(i) for i in input("Enter Input : ").split()]
print(insertion(inp,1,0))