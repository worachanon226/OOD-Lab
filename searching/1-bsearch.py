def bi_search(l, r, arr, x):
    while(l<r):
        if arr[l] < x:
            l += 1
        if arr[r] > x:
            r -= 1
        if arr[r] == x or arr[l] == x:
            return "True"
    return "False"

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))
