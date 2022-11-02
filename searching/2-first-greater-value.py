inp = input('Enter Input : ').split('/')
arr1, arr2 = list(map(int, inp[0].split())), list(map(int, inp[1].split()))

for i in arr2:
    diff,ans = 1000000, None
    for j in arr1:
        if j > i:
            if j-i < diff:
                ans = j
                diff = j-i
    if ans is None:
        print("No First Greater Value")
    else:
        print(ans)
