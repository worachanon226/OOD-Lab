def power(a,b):
    if b != 0:
        return a * power(a,b-1)
    else:
        return 1

inp = input("Enter Input a b : ").split(" ")
ans = power(int(inp[0]),int(inp[1]))
print(ans)