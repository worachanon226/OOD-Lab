def serach(arr,size):
    bx, cnt = 1, 0
    for i in arr:
        if cnt + i <= size:
            cnt += i
        else:
            cnt = i
            bx += 1
    return bx

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
i = max(arr)
while(i):
    bx = serach(arr,i)
    if bx <= k:
        print(f'Minimum weigth for {k} box(es) = {i}')
        break
    i += 1