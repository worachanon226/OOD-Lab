def rng(rn):
    ans = []
    start, end, step = 0.0,0.0,1.0
    lens = rn.split(" ")
    for i in range(0,len(lens)):
        lens[i] = float(lens[i])
    if len(lens) == 1:
        end = lens[0]

    if len(lens) == 2:
        start = lens[0]
        end = lens[1]

    if len(lens) == 3:
        start = lens[0]
        end = lens[1]
        step = lens[2]

    while start < end:
        ans.append(start)
        start += step
    return tuple(ans)


print("*** New Range ***")
rn = input("Enter Input : ")
print(rng(rn))
