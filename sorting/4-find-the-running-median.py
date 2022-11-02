def selection(l):
    for last in range(len(l)-1,0,-1):
        mx, mx_i = l[0], 0
        for i in range(1,last + 1):
            if l[i] > mx:
                mx, mx_i = l[i], i
        if l[last] != l[mx_i]:
            l[last], l[mx_i] = l[mx_i], l[last]   
    return l

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l, ll = list(map(int, l)), []
    for i in range(1,len(l)+1):
        for j in range(i):
            ll.append(l[j])
        ll = selection(ll)
        if len(ll) % 2:
            med = ll[len(ll) // 2]
        else:
            med = ( ll[len(ll) // 2] + ll[len(ll) // 2 - 1] ) / 2
        print(f'list = {l[:j+1]} : median = {float(med)}')
        ll.clear()
    