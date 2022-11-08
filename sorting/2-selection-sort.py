def maxidx( l , i , j ):
    if i == j:
        return i

    k = maxidx(l, i + 1, j)
    return (k if l[i] < l[k] else i)

def selection(l, n):
    if n == 0:
        return 
    k = maxidx(l, 0, n)
     
    if k != n:
        l[k], l[n] = l[n], l[k]
        print(f'swap {l[k]} <-> {l[n]} : {l}')
         
    selection(l, n-1)

inp = [int(i) for i in input("Enter Input : ").split()]
selection(inp,len(inp)-1)
print(inp)