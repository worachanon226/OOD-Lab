mx = -99999

def rng(rn):
    ans = []
    global mx
    start, end, step = 0.0,0.0,1.0
    lens = rn.split(" ")
    for i in range(0,len(lens)):
        lens[i] = str(float(lens[i]))
        ch = lens[i].split(".")[1]
        mx = max(mx,len(ch))
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
        ans.append(round(start,mx))
        start += step

    return tuple(ans)


print("*** New Range ***")
rn = input("Enter Input : ")
print(rng(rn))
