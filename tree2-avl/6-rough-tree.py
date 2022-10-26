inp = input("Enter Input : ").split("/")
n, l, ans = int(inp[0]), [int(i) for i in inp[1].split()], 0

if n//2 + 1 == len(l):
    ll = [None]*(n+1)
    for i in range(n//2+1,n+1):
        ll[i] = l[i-(n//2+1)]
    for i in range(n,0,-1):
        if ll[i] == None:
            mn = min(ll[2*i],ll[2*i+1])
            ll[2*i] -= mn
            ll[2*i+1] -= mn
            ll[i] = mn
    for i in range(1,n+1):
        ans += int(ll[i])
    print(ans)
else:
    print("Incorrect Input")