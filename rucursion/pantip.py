def pantip(k, n, arr, path,cnt):
    if n == len(arr):
        if k == 0:
            cnt+=1
            print(" ".join(str(v) for v in path))
        return cnt
    if arr[n] <= k:
        path.append(arr[n])
        cnt = pantip(k - arr[n], n+1, arr, path,cnt)
        path.pop()
    cnt = pantip(k, n+1, arr, path,cnt)
    return cnt

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [],0)
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))